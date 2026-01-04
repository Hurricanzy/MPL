import re


class JavaToPythonTranslator:
    def __init__(self):
        self.current_context_nesting = 0

    def getIndent(self):
        return "    " * self.current_context_nesting

    def translate(self, code_to_translate):
        lines_to_translate = code_to_translate.splitlines()
        translated_lines = []

        for line in lines_to_translate:
            line = line.strip()

            #  Класс (Пропуск объявление класса, но сохраняем структуру)
            match = re.match(r'^public\s+class\s+(\w+)\s*\{$', line)
            if match:
                class_name = match.group(1)
                translated_lines.append(f"class {class_name}:")
                self.current_context_nesting += 1
                continue

            # Метод main
            match = re.match(r'^public\s+static\s+void\s+main\(String\[\]\s+\w+\)\s*\{$', line)
            if match:
                translated_lines.append(f"{self.getIndent()}@staticmethod")
                translated_lines.append(f"{self.getIndent()}def main():")
                self.current_context_nesting += 1
                continue

            #  Обычные методы
            match = re.match(r'^public\s+static\s+(?:int|void|String|boolean)\s+(\w+)\((.*?)\)\s*\{$', line)
            if match:
                func_name = match.group(1)
                raw_args = match.group(2)
                func_args = []
                if raw_args:
                    for arg in raw_args.split(','):
                        parts = arg.strip().split()
                        if len(parts) >= 2:
                            func_args.append(parts[1])
                        else:
                            func_args.append(parts[0])

                args_str = ", ".join(func_args)
                translated_lines.append(f"{self.getIndent()}@staticmethod")
                translated_lines.append(f"{self.getIndent()}def {func_name}({args_str}):")
                self.current_context_nesting += 1
                continue

            #  Return
            match = re.match(r'^return\s+(.+?);$', line)
            if match:
                return_val = match.group(1)
                translated_lines.append(f"{self.getIndent()}return {return_val}")
                continue

            # Закрывающая скобка
            if line == '}':
                self.current_context_nesting = max(0, self.current_context_nesting - 1)
                continue

            #  Переменные
            match = re.match(r'^(?:int|String|boolean|double)\s+(\w+)\s*=\s*(.+?);$', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2)
                translated_lines.append(f"{self.getIndent()}{var_name} = {var_value}")
                continue

            # Объявление без инициализации
            match = re.match(r'^(?:int|String|boolean|double)\s+(\w+);$', line)
            if match:
                var_name = match.group(1)
                translated_lines.append(f"{self.getIndent()}{var_name} = 0 # Default Java init")
                continue

            #  Операции +=
            match = re.match(r'^(\w+)\s*\+=\s*(.+?);$', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2)
                translated_lines.append(f"{self.getIndent()}{var_name} += {var_value}")
                continue

            #  Вызовы функций
            match = re.match(r'^(?:int|String|boolean|double)\s+(\w+)\s*=\s*(\w+)\((.*?)\);$', line)
            if match:
                var_name = match.group(1)
                func_call = match.group(2)
                args = match.group(3)

                translated_lines.append(f"{self.getIndent()}{var_name} = Simulation.{func_call}({args})")
                continue

            # Простой вызов функции
            match = re.match(r'^(\w+)\((.*?)\);$', line)
            if match:
                func_name = match.group(1)
                args = match.group(2)
                translated_lines.append(f"{self.getIndent()}Simulation.{func_name}({args})")
                continue

            # Цикл for
            match = re.match(r'^for\s*\(int\s+(\w+)\s*=\s*(.+?);\s*\1\s*<\s*(.+?);\s*\1\+\+\)\s*\{$', line)
            if match:
                var_name = match.group(1)
                start_value = match.group(2)
                end_value = match.group(3)
                translated_lines.append(f"{self.getIndent()}for {var_name} in range({start_value}, {end_value}):")
                self.current_context_nesting += 1
                continue

            #  if
            match = re.match(r'^if\s*\((.+?)\)\s*\{$', line)
            if match:
                condition = match.group(1)
                translated_lines.append(f"{self.getIndent()}if {condition}:")
                self.current_context_nesting += 1
                continue

            #  else
            if line == 'else {':
                translated_lines.append(f"{self.getIndent()}else:")
                self.current_context_nesting += 1
                continue

            #  Вывод
            match = re.match(r'^System\.out\.println\((.+?)\);$', line)
            if match:
                text = match.group(1)
                translated_lines.append(f"{self.getIndent()}print({text})")
                continue

            # Если строка пустая
            if not line:
                translated_lines.append("")

        # Добавим запуск main в конце файла
        translated_lines.append("")
        translated_lines.append("if __name__ == '__main__':")
        translated_lines.append("    Simulation.main()")

        self.printToFile(translated_lines)

    def printToFile(self, translated_code):
        with open('translated_from_java.py', 'w', encoding='utf-8') as file:
            file.write("\n".join(translated_code))


if __name__ == '__main__':
    try:
        with open("input.java", 'r', encoding="utf-8") as f:
            code = f.read()

        translator = JavaToPythonTranslator()
        translator.translate(code)

        print("Результирующий перевод сохранен в файл translated_from_java.py")
    except FileNotFoundError:
        print("Ошибка: Файл input.java не найден.")