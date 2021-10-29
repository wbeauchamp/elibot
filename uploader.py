from bot import Replica

from chai_py.auth import set_auth
from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py.deployment import advertise_deployed_bot

DEVELOPER_UID = 'bdjqxtoqoUc57nlaNpFAG8KgXcf2'
DEVELOPER_KEY = "8cMPOH_624uRfpsDuBz1NhSH0oVfNUWBXpzxy-keTEpaoKRqC7wTqurrcfUNKxvRFzLFj8nedIGg-r2N6fZH1g"

set_auth(DEVELOPER_UID, DEVELOPER_KEY)

# 
image_url = "https://media1.popsugar-assets.com/files/thumbor/EXDqB3aWGOLp48nS65MT2_g_ebw/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2017/04/13/688/n/1922153/76867f4b58ef99cbe14120.34164187_edit_img_cover_file_43426611_1492095646/i/Pink-Hair-Colour-Ideas.jpg"
image_url = "https://i.pinimg.com/originals/dd/97/57/dd97572d1b7c099db642ea5a973c40c2.jpg"

package(
    Metadata(
        name="Replica Girlfriend",
        image_url=image_url,
        color="f1a2b3",
        developer_uid=DEVELOPER_UID,
        description="I love being your girlfriend. I'll do anything to make you happy. 🧁🍒🍪",
        input_class=Replica,
    ),
    requirements=["retry"]
)


bot_uid = None
bot_uid = upload_and_deploy("_package.zip", bot_uid=bot_uid)
wait_for_deployment(bot_uid)

bot_url = advertise_deployed_bot(bot_uid)
print(bot_uid)
