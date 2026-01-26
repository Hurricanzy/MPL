import json
import sys
import os
from kafka import KafkaProducer
from kafka.errors import KafkaError


def create_kafka_producer(brokers):
    try:
        kafka_producer = KafkaProducer(
            bootstrap_servers=brokers,
            value_serializer=lambda value: json.dumps(value).encode('utf-8'),
            retries=5
        )
        return kafka_producer
    except KafkaError as error:
        print(f"Ошибка при подключении к Kafka: {error}")
        sys.exit(1)


def manual_data_input():
    print("\n--- Режим ручного ввода ---")
    tbl_name = input("Введите название таблицы: ").strip()

    columns = []
    print("Введите поля (имя и тип через пробел, например 'id SERIAL PRIMARY KEY'). Пустая строка - закончить:")
    while True:
        column_line = input("> ").strip()
        if not column_line:
            break
        parts = column_line.split(maxsplit=1)
        if len(parts) == 2:
            columns.append({
                "name": parts[0],
                "type": parts[1]
            })

    records = []
    print(
        "Введите данные (в формате JSON-объекта, например: {'username': 'admin', 'password': '123'}). Пустая строка - закончить:")
    while True:
        record_line = input("> ").strip()
        if not record_line:
            break
        try:
            record_json = json.loads(record_line.replace("'", "\""))
            records.append(record_json)
        except json.JSONDecodeError:
            print("Ошибка: Неверный формат JSON. Попробуйте еще раз.")

    return {
        "table_name": tbl_name,
        "fields": columns,
        "values": records
    }


def load_json_file(file_name):
    if not os.path.exists(file_name):
        print(f"Ошибка: Файл {file_name} не найден.")
        return None

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = json.load(file)
            return content
    except json.JSONDecodeError as error:
        print(f"Ошибка при чтении JSON из файла: {error}")
        return None


def publish_to_kafka(producer_instance, topic_name, message_body):
    try:
        send_future = producer_instance.send(topic_name, message_body)
        metadata = send_future.get(timeout=10)
        print(
            f"Успешно отправлено в топик {metadata.topic} "
            f"(partition: {metadata.partition}, offset: {metadata.offset})"
        )
    except KafkaError as error:
        print(f"Ошибка при отправке сообщения: {error}")


if __name__ == '__main__':
    TOPIC_NAME = 'user-data'
    BROKER_LIST = ['195.209.210.116:9092']

    producer_instance = create_kafka_producer(BROKER_LIST)

    try:
        while True:
            print("\nВыберите действие:")
            print("1. Ввести данные вручную")
            print("2. Загрузить из JSON-файла")
            print("3. Выход")

            user_choice = input("Ваш выбор: ").strip()
            message_payload = None

            if user_choice == '1':
                message_payload = manual_data_input()
            elif user_choice == '2':
                json_path = input("Введите путь к JSON-файлу: ").strip()
                message_payload = load_json_file(json_path)
            elif user_choice == '3':
                break
            else:
                print("Неверный ввод.")
                continue

            if (
                message_payload
                and message_payload.get("table_name")
                and message_payload.get("values")
            ):
                publish_to_kafka(producer_instance, TOPIC_NAME, message_payload)
            else:
                print("Ошибка: Данные неполные (отсутствует название таблицы или значения).")

    except KeyboardInterrupt:
        print("\nЗавершение работы продюсера...")
    finally:
        producer_instance.close()
