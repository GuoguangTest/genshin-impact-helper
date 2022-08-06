# settings
import logging

import os

__all__ = ['log', 'CONFIG']

log = logger = logging


class _Config:
    ACT_ID = 'e202009291139501'
    APP_VERSION = '2.34.1'
    REFERER_URL = 'https://webstatic.mihoyo.com/bbs/event/signin-ys/index.html?' \
                  'bbs_auth_required={}&act_id={}&utm_source={}&utm_medium={}&' \
                  'utm_campaign={}'.format('true', ACT_ID, 'bbs', 'mys', 'icon')
    AWARD_URL = 'https://api-takumi.mihoyo.com/event/bbs_sign_reward/home?act_id={}'.format(ACT_ID)
    ROLE_URL = 'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz={}'.format('hk4e_cn')
    INFO_URL = 'https://api-takumi.mihoyo.com/event/bbs_sign_reward/info?region={}&act_id={}&uid={}'
    SIGN_URL = 'https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign'
    USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'miHoYoBBS/{}'.format(APP_VERSION)


class ProductionConfig(_Config):
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(_Config):
    LOG_LEVEL = logging.DEBUG


RUN_ENV = os.environ.get('RUN_ENV', 'prod')
if RUN_ENV == 'dev':
    CONFIG = DevelopmentConfig()
else:
    CONFIG = ProductionConfig()

log.basicConfig(
    level=CONFIG.LOG_LEVEL,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')

MESSAGE_TEMPLATE = '''
    {today:#^28}
    🔅[{region_name}]{uid}
    今日奖励: {award_name} × {award_cnt}
    本月累签: {total_sign_day} 天
    签到结果: {status}
    {end:#^28}'''

CONFIG.MESSAGE_TEMPLATE = MESSAGE_TEMPLATE
