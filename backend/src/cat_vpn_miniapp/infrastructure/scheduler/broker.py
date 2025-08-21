import logging

from taskiq import TaskiqEvents, TaskiqScheduler, TaskiqState
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_redis import ListRedisScheduleSource, RedisStreamBroker

from cat_vpn_miniapp.bootstrap.config import Config

config = Config()

broker = RedisStreamBroker(url=config.redis_config.redis_url)

redis_source = ListRedisScheduleSource(url=config.redis_config.redis_url)

scheduler = TaskiqScheduler(broker, [redis_source, LabelScheduleSource(broker)])

logger = logging.getLogger(__name__)


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState):
    logger.info("startup Scheduler")


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown(state: TaskiqState):
    logger.info("shutdown Scheduler")
