import logging
import click
from dotenv import load_dotenv

from udata_analysis_service.consumer import consume_kafka
from udata_analysis_service.background_tasks import celery


@click.group()
@click.version_option()
def cli() -> None:
    """
    udata-analysis-service
    """


@cli.command()
def consume() -> None:
    """Launch Kafka consumer loop"""
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    consume_kafka()


@cli.command()
def work() -> None:
    """Starts a worker"""
    worker = celery.Worker()
    worker.start()
    return worker.exitcode
