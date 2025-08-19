import logging

from taskiq import TaskiqEvents, TaskiqScheduler, TaskiqState
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_redis import ListRedisScheduleSource, RedisStreamBroker

broker = RedisStreamBroker("redis://redis:6379")

redis_source = ListRedisScheduleSource(url="redis://redis:6379")

scheduler = TaskiqScheduler(broker, [redis_source, LabelScheduleSource(broker)])

logger = logging.getLogger(__name__)


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState):
    logger.info("startup Scheduler")


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown(state: TaskiqState):
    logger.info("shutdown Scheduler")
