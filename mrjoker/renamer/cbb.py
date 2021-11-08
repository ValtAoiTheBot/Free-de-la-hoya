import pyrogram

from mrjoker.renamer import rename_cb, cancel_extract, send_start
from mrjoker.renamer import force_name
from script import script


@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)
        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
