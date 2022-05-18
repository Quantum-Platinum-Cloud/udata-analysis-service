import logging
import os

from udata_analysis_service.background_tasks import manage_resource


def process_message(message: dict) -> None:
    resource_id = message.key.decode("utf-8")
    logging.info(f"New message detected, checking resource {resource_id}")

    dataset_id = message["meta"]["dataset_id"]
    manage_resource.delay(
        dataset_id,
        resource_id,
        message["value"]["location"],
        minio_user=os.environ["MINIO_USER"],
        minio_pwd=os.environ["MINIO_PWD"],
    )
