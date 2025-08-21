import logging

from aiogram import Bot
from dishka import FromDishka
from dishka.integrations.taskiq import inject
from fluentogram import TranslatorRunner

from cat_vpn_miniapp.application.services import UserService
from cat_vpn_miniapp.domain.config import Config
from cat_vpn_miniapp.infrastructure.scheduler.broker import broker

logger = logging.getLogger(__name__)


@broker.task(task_name="notify_about_users_with_expiring_keys", schedule=[{"cron": "0 9 * * *"}])
@inject(patch_module=True)
async def process_users_with_expiring_keys(
        user_service: FromDishka[UserService],
        i18n: FromDishka[TranslatorRunner],
):
    users = await user_service.get_users_with_expiring_keys()
    logger.info(F"found {len(users)} users")
    for user in users:
        text = i18n.key.expiring(name=user.first_name, valid_until=user.key.valid_until)
        await notify_user_about_with_expiring_key.kiq(tid=user.tid, text=text)

    if users:
        admin_text = i18n.notify.users_expiring(user_ids=", ".join(str(user.tid) for user in users))

        await send_message_to_admins.kiq(admin_text)


@broker.task(task_name="send_message_to_admin")
@inject(patch_module=True)
async def send_message_to_admins(
        admin_text: str,
        bot: FromDishka[Bot],
        config: FromDishka[Config],
):
    admin_ids = [int(admin_id) for admin_id in config.bot_config.admin_ids.split(",") if admin_id]
    for admin_id in admin_ids:
        await bot.send_message(chat_id=admin_id, text=admin_text)


@broker.task(task_name="notify_user_about_with_expiring_key")
@inject(patch_module=True)
async def notify_user_about_with_expiring_key(
        tid: int,
        text: str,
        bot: FromDishka[Bot],
):
    await bot.send_message(chat_id=tid, text=text)
