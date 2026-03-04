###############################################
##  CopyRight & Creator File And Programing  ##
##                                           ##
##     #######  ######  #####*     *##*      ##
##     #  #  #  ###     #     *   *    *     ##
##     #     #  ##      #     *   *    *     ##
##     #     #  #####   #####*     *##*      ##
##                                           ##
###############################################

################################
## Dev By: @S550D & @ttccss ##
################################

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information


@Client.on_callback_query(filters.regex("^music (\\d+)$"))
async def music(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="araby " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("• اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^music2 (\\d+)$"))
async def music2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="araby " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^araby (\\d+)$"))
async def araby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("محمد سعيد 🔊", callback_data="mhrgan " + str(m.from_user.id))] +
        [InlineKeyboardButton("عصام صاصا 🔊", callback_data="adham " + str(m.from_user.id))],
        [InlineKeyboardButton("عمر كمال 🔊", callback_data="Fasw " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد منير 🔊", callback_data="tamer " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلم حزين 🔊", callback_data="rran " + str(m.from_user.id))] +
        [InlineKeyboardButton("مسلم مهرجان 🔊", callback_data="pplal " + str(m.from_user.id))],
        [InlineKeyboardButton("احمد كامل 🔊", callback_data="kawiw " + str(m.from_user.id))] +
        [InlineKeyboardButton("عمرو دياب 🔊", callback_data="woasa " + str(m.from_user.id))],
        [InlineKeyboardButton("اليسا 🔊", callback_data="swlesa " + str(m.from_user.id))] +
        [InlineKeyboardButton("اصاله 🔊", callback_data="owjzw " + str(m.from_user.id))],
        [InlineKeyboardButton("بابلو 🔊", callback_data="ohby " + str(m.from_user.id))] +
        [InlineKeyboardButton("عمار حسني 🔊", callback_data="dmar " + str(m.from_user.id))],
        [InlineKeyboardButton("حمو بيكا 🔊", callback_data="mjoker " + str(m.from_user.id))] +
        [InlineKeyboardButton("عفريتو 🔊", callback_data="oker " + str(m.from_user.id))],
        [InlineKeyboardButton("حماقي 🔊", callback_data="ownanw " + str(m.from_user.id))] +
        [InlineKeyboardButton("ويجز 🔊", callback_data="Rapwd " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اهلا بك بقائمه الفنانين اختر احدي المغنيين\n√", reply_markup=keyboard)



@Client.on_callback_query(filters.regex("^mhrgan (\\d+)$"))
async def mhrgan(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("ماتستغربيش 🎧", callback_data="Xmhrg1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قالوا عليكي 🎧", callback_data="Xmhrg2 " + str(m.from_user.id))],
        [InlineKeyboardButton("محتاج لوجودك 🎧", callback_data="Xmhrg3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("غيبي 🎧", callback_data="Xmhrg4 " + str(m.from_user.id))],
        [InlineKeyboardButton("لو 🎧", callback_data="Xmhrg5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لو ما الك يفلان 🎧", callback_data="Xmhrg6 " + str(m.from_user.id))],
        [InlineKeyboardButton("مكملناش 🎧", callback_data="Xmhrg7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بيني وبينك 🎧", callback_data="Xmhrg8 " + str(m.from_user.id))],
        [InlineKeyboardButton("جواكي 🎧", callback_data="Xmhrg9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نانسي 🎧", callback_data="Xmhrg10 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة محمد سعيد 1\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xmhrg1 (\\d+)$"))
async def Xmhrg1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/40", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmhrg2 (\\d+)$"))
async def Xmhrg2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/41", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmhrg3 (\\d+)$"))
async def Xmhrg3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/42", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmhrg4 (\\d+)$"))
async def Xmhrg4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/43", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmhrg5 (\\d+)$"))
async def Xmhrg5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/44", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmhrg6 (\\d+)$"))
async def Xmhrg6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/45", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmhrg7 (\\d+)$"))
async def Xmhrg7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/46", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmhrg8 (\\d+)$"))
async def Xmhrg8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/47", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmhrg9 (\\d+)$"))
async def Xmhrg9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/48", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmhrg10 (\\d+)$"))
async def Xmhrg10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/49", reply_to_message_id=mid)

########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^adham (\\d+)$"))
async def adham(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اه يابخته اللي يزاملني 🎧", callback_data="Xadh1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كله غلطه 🎧", callback_data="Xadh2 " + str(m.from_user.id))],
        [InlineKeyboardButton("هولعه اون فاير 🎧", callback_data="Xadh3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ندمان عارف ياباشا 🎧", callback_data="Xadh4 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصحاب دول غدارين 🎧", callback_data="Xadh5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انتي حبك تمثليه 🎧", callback_data="Xadh6 " + str(m.from_user.id))],
        [InlineKeyboardButton("خطفت الجو 🎧", callback_data="Xadh7 " + str(m.from_user.id))],
        [InlineKeyboardButton("ميت انا مش عارفني 🎧", callback_data="Xadh8 " + str(m.from_user.id))],
        [InlineKeyboardButton("كله سابني بقيت لوحدي 🎧", callback_data="Xadh9 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياه لو اموت دقيقه 🎧", callback_data="Xadh10 " + str(m.from_user.id))],
        [InlineKeyboardButton("اه يبختو الي يزملني 🎧", callback_data="Xadh11 " + str(m.from_user.id))],        

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني عصام صاصا", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^Xadh1 (\\d+)$"))
async def Xadh1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/26", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh2 (\\d+)$"))
async def Xadh2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/27", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh3 (\\d+)$"))
async def Xadh3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/28", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh4 (\\d+)$"))
async def Xadh4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/29", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh5 (\\d+)$"))
async def Xadh5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/30", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh6 (\\d+)$"))
async def Xadh6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/31", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh7 (\\d+)$"))
async def Xadh7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/32", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh8 (\\d+)$"))
async def Xadh8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/33", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh9 (\\d+)$"))
async def Xadh9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/34", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xadh10 (\\d+)$"))
async def Xadh10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/35", reply_to_message_id=mid)
    
    
@Client.on_callback_query(filters.regex("^Xadh11 (\\d+)$"))
async def Xadh11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/36", reply_to_message_id=mid)
######################################################################
######################################################################

########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^dmar (\\d+)$"))
async def dmar(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("بتيجي في بالي 🎧", callback_data="Xamm1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طيب 🎧", callback_data="Xamm2 " + str(m.from_user.id))],
        [InlineKeyboardButton("برشامه منوم 🎧", callback_data="Xamm3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بساط 🎧", callback_data="Xamm4 " + str(m.from_user.id))],
        [InlineKeyboardButton("طفره 🎧", callback_data="Xamm5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ترام 🎧", callback_data="Xamm6 " + str(m.from_user.id))],
        [InlineKeyboardButton("هلوسه 🎧", callback_data="Xamm7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مسوخ 🎧", callback_data="Xamm8 " + str(m.from_user.id))],
        [InlineKeyboardButton("بلاش تغني 🎧", callback_data="Xamm9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اخر عازف ع الارض 🎧", callback_data="Xamm10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حدود 🎧", callback_data="Xamm11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("غامق 🎧", callback_data="Xamm12 " + str(m.from_user.id))],
        [InlineKeyboardButton("فاترينا 🎧", callback_data="Xamm13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جهنم 🎧", callback_data="Xamm14 " + str(m.from_user.id))],
        [InlineKeyboardButton("فستان 🎧", callback_data="Xamm15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ضي العين 🎧", callback_data="Xamm16 " + str(m.from_user.id))],
        [InlineKeyboardButton("يا ليل اندهلي 🎧", callback_data="Xamm17 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني عمار حسني", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xamm1 (\\d+)$"))
async def Xamm1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/177", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm2 (\\d+)$"))
async def Xamm2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/178", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm3 (\\d+)$"))
async def Xamm3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/179", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm4 (\\d+)$"))
async def Xamm4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/180", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm5 (\\d+)$"))
async def Xamm5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/181", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm6 (\\d+)$"))
async def Xamm6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/182", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm7 (\\d+)$"))
async def Xamm7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/183", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm8 (\\d+)$"))
async def Xamm8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/184", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm9 (\\d+)$"))
async def Xamm9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/185", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm10 (\\d+)$"))
async def Xamm10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/186", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm11 (\\d+)$"))
async def Xamm11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/187", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm12 (\\d+)$"))
async def Xamm12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/188", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm13 (\\d+)$"))
async def Xamm13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/189", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm14 (\\d+)$"))
async def Xamm14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/190", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm15 (\\d+)$"))
async def Xamm15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/191", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm16 (\\d+)$"))
async def Xamm16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/192", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xamm17 (\\d+)$"))
async def Xamm17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/193", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^woasa (\\d+)$"))
async def woasa(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("وياه 🎧", callback_data="Xasa1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وماله 🎧", callback_data="Xasa2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضحكت 🎧", callback_data="Xasa3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جماله 🎧", callback_data="Xasa4 " + str(m.from_user.id))],
        [InlineKeyboardButton("قمرين 🎧", callback_data="Xasa5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نور العين 🎧", callback_data="Xasa6 " + str(m.from_user.id))],
        [InlineKeyboardButton("سنين 🎧", callback_data="Xasa7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عودني 🎧", callback_data="Xasa8 " + str(m.from_user.id))],
        [InlineKeyboardButton("باين حبيت 🎧", callback_data="Xasa9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("من العشم 🎧", callback_data="Xasa10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني عمرو دياب 🔊\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xasa1 (\\d+)$"))
async def Xasa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/118", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa2 (\\d+)$"))
async def Xasa2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/119", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa3 (\\d+)$"))
async def Xasa3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/120", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa4 (\\d+)$"))
async def Xasa4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/121", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa5 (\\d+)$"))
async def Xasa5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/122", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa6 (\\d+)$"))
async def Xasa6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/123", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa7 (\\d+)$"))
async def Xasa7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/124", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa8 (\\d+)$"))
async def Xasa8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/125", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa9 (\\d+)$"))
async def Xasa9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/126", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa10 (\\d+)$"))
async def Xasa10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/127", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^kawiw (\\d+)$"))
async def kawiw(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("علي عيني 🎧", callback_data="Xbab1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اكتر من السكوت 🎧", callback_data="Xbab2 " + str(m.from_user.id))],
        [InlineKeyboardButton("لعبتك 🎧", callback_data="Xbab3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قولي 🎧", callback_data="Xbab4 " + str(m.from_user.id))],
        [InlineKeyboardButton("مبقتش اخاف 🎧", callback_data="Xbab5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مين في دول 🎧", callback_data="Xbab6 " + str(m.from_user.id))],
        [InlineKeyboardButton("كان في طفل 🎧", callback_data="Xbab7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ياليل 🎧", callback_data="Xbab8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني احمد كامل\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xbab1 (\\d+)$"))
async def Xbab1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/109", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab2 (\\d+)$"))
async def Xbab2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/110", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab3 (\\d+)$"))
async def Xbab3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/111", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab4 (\\d+)$"))
async def Xbab4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/112", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab5 (\\d+)$"))
async def Xbab5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/113", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab6 (\\d+)$"))
async def Xbab6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/114", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab7 (\\d+)$"))
async def Xbab7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/115", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xbab8 (\\d+)$"))
async def Xbab8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/116", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^ownanw (\\d+)$"))
async def ownanw(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هو ده حبيبي 🎧", callback_data="Xham1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قدام الناس 🎧", callback_data="Xham2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياستار 🎧", callback_data="Xham3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("راسمك في خيالي 🎧", callback_data="Xham4 " + str(m.from_user.id))],
        [InlineKeyboardButton("احلي حاجه فيكي 🎧", callback_data="Xham5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مابلاش 🎧", callback_data="Xham6 " + str(m.from_user.id))],
        [InlineKeyboardButton("م البدايه 🎧", callback_data="Xham7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليله باظت 🎧", callback_data="Xham8 " + str(m.from_user.id))],
        [InlineKeyboardButton("واحده واحده 🎧", callback_data="Xham9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("واعمل ايه 🎧", callback_data="Xham10 " + str(m.from_user.id))],
        [InlineKeyboardButton("من قلبي بغني 🎧", callback_data="Xham11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حاجه مستخبيه 🎧", callback_data="Xham12 " + str(m.from_user.id))],
        
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني حماقي\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xham1 (\\d+)$"))
async def Xham1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/152", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham2 (\\d+)$"))
async def Xham2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/153", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham3 (\\d+)$"))
async def Xham3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/154", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham4 (\\d+)$"))
async def Xham4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/155", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham5 (\\d+)$"))
async def Xham5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/156", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham6 (\\d+)$"))
async def Xham6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/157", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham7 (\\d+)$"))
async def Xham7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/158", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham8 (\\d+)$"))
async def Xham8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/159", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham9 (\\d+)$"))
async def Xham9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/160", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham10 (\\d+)$"))
async def Xham10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/161", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham11 (\\d+)$"))
async def Xham11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/162", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xham12 (\\d+)$"))
async def Xham12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/163", reply_to_message_id=mid)




########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^swlesa (\\d+)$"))
async def swlesa(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("يا مرايتي 🎧", callback_data="Xeles1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("افتكرت 🎧", callback_data="Xeles2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مكتوبه ليك 🎧", callback_data="Xeles3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حاله حب 🎧", callback_data="Xeles4 " + str(m.from_user.id))],
        [InlineKeyboardButton("تعبت منك 🎧", callback_data="Xeles5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وانت قصادي 🎧", callback_data="Xeles6 " + str(m.from_user.id))],
        [InlineKeyboardButton("مباحه ليك 🎧", callback_data="Xeles7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("في عيونك 🎧", callback_data="Xeles8 " + str(m.from_user.id))],
        [InlineKeyboardButton("انا شبه نسيتك 🎧", callback_data="Xeles9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنحب الحياه 🎧", callback_data="Xeles10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حبه اهتمام 🎧", callback_data="Xeles11 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني اليسا\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xeles1 (\\d+)$"))
async def Xeles1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/129", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles2 (\\d+)$"))
async def Xeles2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/130", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles3 (\\d+)$"))
async def Xeles3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/131", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles4 (\\d+)$"))
async def Xeles4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/132", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles5 (\\d+)$"))
async def Xeles5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/133", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles6 (\\d+)$"))
async def Xeles6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/134", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles7 (\\d+)$"))
async def Xeles7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/135", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles8 (\\d+)$"))
async def Xeles8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/136", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles9 (\\d+)$"))
async def Xeles9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/137", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles10 (\\d+)$"))
async def Xeles10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/138", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xeles11 (\\d+)$"))
async def Xeles11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/139", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^oker (\\d+)$"))
async def oker(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("برازيل 🎧", callback_data="zxcv1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فرق خبرة 🎧", callback_data="zxcv2 " + str(m.from_user.id))],
        [InlineKeyboardButton("تيجي جون 🎧", callback_data="zxcv3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سان ستيفانو 🎧", callback_data="zxcv4 " + str(m.from_user.id))],
        [InlineKeyboardButton("نابلم 🎧", callback_data="zxcv5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انا ديل 🎧", callback_data="zxcv6 " + str(m.from_user.id))],
        [InlineKeyboardButton("فريسكا 🎧", callback_data="zxcv7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قهوجي 🎧", callback_data="zxcv8 " + str(m.from_user.id))],
        [InlineKeyboardButton("مش بالحظوظ 🎧", callback_data="zxcv9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("واعمل ايه 🎧", callback_data="zxcv10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني عفريتو\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^zxcv1 (\\d+)$"))
async def zxcv1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/212", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv2 (\\d+)$"))
async def zxcv2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/213", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv3 (\\d+)$"))
async def zxcv3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/214", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv4 (\\d+)$"))
async def zxcv4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/215", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv5 (\\d+)$"))
async def zxcv5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/216", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv6 (\\d+)$"))
async def zxcv6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/217", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv7 (\\d+)$"))
async def zxcv7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/218", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv8 (\\d+)$"))
async def zxcv8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/219", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv9 (\\d+)$"))
async def zxcv9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/220", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^zxcv10 (\\d+)$"))
async def zxcv10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/220", reply_to_message_id=mid)




########################################################################################################################
########################################################################################################################




#######################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^mjoker (\\d+)$"))
async def mjoker(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("تلاشاني 🎧", callback_data="Xjok1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انا بكبك المهم 🎧", callback_data="Xjok2 " + str(m.from_user.id))],
        [InlineKeyboardButton("كل الجيهات خصمت 🎧", callback_data="Xjok3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كل العنابر تحضرلي 🎧", callback_data="Xjok4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ده الحب فيكي صحه 🎧", callback_data="Xjok5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يا شويه جواجع 🎧", callback_data="Xjok6 " + str(m.from_user.id))],
        [InlineKeyboardButton("النسور ع الدبابات 🎧", callback_data="Xjok7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشرقيه خطر 🎧", callback_data="Xjok8 " + str(m.from_user.id))],
        [InlineKeyboardButton("اصحاب المال 🎧", callback_data="Xjok9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مشاغب وصولي 🎧", callback_data="Xjok10 " + str(m.from_user.id))],
        [InlineKeyboardButton("وسع للبطل 🎧", callback_data="Xjok11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مخنوق 🎧", callback_data="Xjok12 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني حمو بيكا\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xjok1 (\\d+)$"))
async def Xjok1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/195", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok2 (\\d+)$"))
async def Xjok2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/196", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok3 (\\d+)$"))
async def Xjok3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/197", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok4 (\\d+)$"))
async def Xjok4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/198", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok5 (\\d+)$"))
async def Xjok5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/199", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok6 (\\d+)$"))
async def Xjok6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/200", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok7 (\\d+)$"))
async def Xjok7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/201", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok8 (\\d+)$"))
async def Xjok8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/202", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok9 (\\d+)$"))
async def Xjok9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/203", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok10 (\\d+)$"))
async def Xjok10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/204", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok11 (\\d+)$"))
async def Xjok11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/205", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xjok12 (\\d+)$"))
async def Xjok12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/206", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^Rapwd (\\d+)$"))
async def Rapwd(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اميره 🎧", callback_data="Xkam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تايه 🎧", callback_data="Xkam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("حصري 🎧", callback_data="Xkam3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عفاريت الاسفلت 🎧", callback_data="Xkam4 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجراند طوطو 🎧", callback_data="Xkam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تراب كينج 🎧", callback_data="Xkam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("بعوده يا بلادي 🎧", callback_data="Xkam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كان نفسي تجوبيني 🎧", callback_data="Xkam8 " + str(m.from_user.id))],
        [InlineKeyboardButton("فريسكا 🎧", callback_data="Xkam9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اسياد الصوت 🎧", callback_data="Xkam10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني احمد كامل\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xkam1 (\\d+)$"))
async def Xkam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/165", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam2 (\\d+)$"))
async def Xkam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/166", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam3 (\\d+)$"))
async def Xkam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/167", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam4 (\\d+)$"))
async def Xkam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/168", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam5 (\\d+)$"))
async def Xkam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/169", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam6 (\\d+)$"))
async def Xkam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/170", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam7 (\\d+)$"))
async def Xkam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/171", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam8 (\\d+)$"))
async def Xkam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/172", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam9 (\\d+)$"))
async def Xkam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/173", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xkam10 (\\d+)$"))
async def Xkam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/174", reply_to_message_id=mid)



########################################################################################################################
########################################################################################################################




########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^owjzw (\\d+)$"))
async def owjzw(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

       [InlineKeyboardButton("60 دقيقه 🎧", callback_data="Xasa1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("خانات الذكريات 🎧", callback_data="Xasa2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياعالم 🎧", callback_data="Xasa3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هو حبيبي 🎧", callback_data="Xasa4 " + str(m.from_user.id))],
        [InlineKeyboardButton("قد الحروف 🎧", callback_data="Xasa5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اسفه 🎧", callback_data="Xasa6 " + str(m.from_user.id))],
        [InlineKeyboardButton("اكتر 🎧", callback_data="Xasa7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جابو سيرتو 🎧", callback_data="Xasa8 " + str(m.from_user.id))],
        [InlineKeyboardButton("روحي وخداني 🎧", callback_data="Xasa9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سؤال بسيط 🎧", callback_data="Xasa10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني اصاله\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xasa1 (\\d+)$"))
async def Xasa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/141", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa2 (\\d+)$"))
async def Xasa2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/142", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa3 (\\d+)$"))
async def Xasa3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/143", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa4 (\\d+)$"))
async def Xasa4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/144", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa5 (\\d+)$"))
async def Xasa5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/145", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa6 (\\d+)$"))
async def Xasa6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/146", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa7 (\\d+)$"))
async def Xasa7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/147", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa8 (\\d+)$"))
async def Xasa8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/148", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa9 (\\d+)$"))
async def Xasa9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/149", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xasa10 (\\d+)$"))
async def Xasa10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/150", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^ohby (\\d+)$"))
async def ohby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الجميزه 🎧", callback_data="Xsahb1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فري 🎧", callback_data="Xsahb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("سندباد 🎧", callback_data="Xsahb3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ابو مكة 🎧", callback_data="Xsahb4 " + str(m.from_user.id))],
        [InlineKeyboardButton("افتر بارتي 🎧", callback_data="Xsahb5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سكانيا 🎧", callback_data="Xsahb6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ديناميت 🎧", callback_data="Xsahb7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فولكلور 🎧", callback_data="Xsahb8 " + str(m.from_user.id))],
  
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة الاغاني بابلو\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xsahb1 (\\d+)$"))
async def Xsahb1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/222", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb2 (\\d+)$"))
async def Xsahb2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/223", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb3 (\\d+)$"))
async def Xsahb3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/224", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb4 (\\d+)$"))
async def Xsahb4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/225", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb5 (\\d+)$"))
async def Xsahb5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/226", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb6 (\\d+)$"))
async def Xsahb6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/227", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb7 (\\d+)$"))
async def Xsahb7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/228", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xsahb8 (\\d+)$"))
async def Xsahb8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/229", reply_to_message_id=mid)




########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^tamer (\\d+)$"))
async def tamer(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("للي 🎧", callback_data="Xtam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انا رايق 🎧", callback_data="Xtam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("حرام 🎧", callback_data="Xtam3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وعدني 🎧", callback_data="Xtam4 " + str(m.from_user.id))],
        [InlineKeyboardButton("اللي باقي من صحابي 🎧", callback_data="Xtam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("باب الجمال 🎧", callback_data="Xtam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("فينك ياحبيبي 🎧", callback_data="Xtam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("في عشق البنات 🎧", callback_data="Xtam8 " + str(m.from_user.id))],
        [InlineKeyboardButton("الليلة ياسمرة 🎧", callback_data="Xtam9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكينج 🎧", callback_data="Xtam10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حارة السقايين 🎧", callback_data="Xtam11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طاق طاقيه 🎧", callback_data="Xtam12 " + str(m.from_user.id))],
        [InlineKeyboardButton("صوتك 🎧", callback_data="Xtam13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شبابيك 🎧", callback_data="Xtam14 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🎧", callback_data="Xtam15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لما النسيم 🎧", callback_data="Xtam16 " + str(m.from_user.id))],
        [InlineKeyboardButton("خايف 🎧", callback_data="Xtam17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يا حمام 🎧", callback_data="Xtam18 " + str(m.from_user.id))],
        [InlineKeyboardButton("يا طير يا طاير 🎧", callback_data="Xtam19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اه ياسمراني 🎧", callback_data="Xtam20 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني محمد منير\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xtam1 (\\d+)$"))
async def Xtam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/65", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam2 (\\d+)$"))
async def Xtam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/66", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam3 (\\d+)$"))
async def Xtam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/67", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam4 (\\d+)$"))
async def Xtam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/68", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam5 (\\d+)$"))
async def Xtam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/69", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam6 (\\d+)$"))
async def Xtam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/70", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam7 (\\d+)$"))
async def Xtam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/71", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam8 (\\d+)$"))
async def Xtam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/72", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam9 (\\d+)$"))
async def Xtam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/73", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam10 (\\d+)$"))
async def Xtam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/74", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam11 (\\d+)$"))
async def Xtam11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/75", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam12 (\\d+)$"))
async def Xtam12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/76", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam13 (\\d+)$"))
async def Xtam13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/77", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam14 (\\d+)$"))
async def Xtam14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/78", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam15 (\\d+)$"))
async def Xtam15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/79", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam16 (\\d+)$"))
async def Xtam16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/80", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam17 (\\d+)$"))
async def Xtam17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/81", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam18 (\\d+)$"))
async def Xtam18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/82", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam19 (\\d+)$"))
async def Xtam19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/83", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xtam20 (\\d+)$"))
async def Xtam20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/84", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################



@Client.on_callback_query(filters.regex("^Fasw (\\d+)$"))
async def Fasw(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("انتي قلبي وربنا 🎧", callback_data="Xweg1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انت اخترت 🎧", callback_data="Xweg2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مش مخلصين 🎧", callback_data="Xweg3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ضيعنا 🎧", callback_data="Xweg4 " + str(m.from_user.id))],
        [InlineKeyboardButton("خلينا سهرانين 🎧", callback_data="Xweg5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قد الظروف 🎧", callback_data="Xweg6 " + str(m.from_user.id))],
        [InlineKeyboardButton("انتي قطتي 🎧", callback_data="Xweg7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يلا سلام 🎧", callback_data="Xweg8 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكدابين 🎧", callback_data="Xweg9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الغربة 🎧", callback_data="Xweg10 " + str(m.from_user.id))],
        [InlineKeyboardButton("بنتخان 🎧", callback_data="Xweg11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اللي تقلان عليك 🎧", callback_data="Xweg12 " + str(m.from_user.id))],
        [InlineKeyboardButton("لا ابالي 🎧", callback_data="Xweg13 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني عمر كمال\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xweg1 (\\d+)$"))
async def Xweg1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/51", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg2 (\\d+)$"))
async def Xweg2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/52", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg3 (\\d+)$"))
async def Xweg3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/53", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg4 (\\d+)$"))
async def Xweg4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/54", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg5 (\\d+)$"))
async def Xweg5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/55", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg6 (\\d+)$"))
async def Xweg6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/56", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg7 (\\d+)$"))
async def Xweg7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/57", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg8 (\\d+)$"))
async def Xweg8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/58", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg9 (\\d+)$"))
async def Xweg9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/59", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg10 (\\d+)$"))
async def Xweg10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/60", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg11 (\\d+)$"))
async def Xweg11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/61", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg12 (\\d+)$"))
async def Xweg12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/62", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xweg13 (\\d+)$"))
async def Xweg13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/63", reply_to_message_id=mid)

########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^rran (\\d+)$"))
async def helal(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مش ندمان 🎧", callback_data="Xhela1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مين كان سبب 🎧", callback_data="Xhela2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ما بهربش 🎧", callback_data="Xhela3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قبل ما اوصلك 🎧", callback_data="Xhela4 " + str(m.from_user.id))],
        [InlineKeyboardButton("لو بس نرجع 🎧", callback_data="Xhela5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("معادش باقي 🎧", callback_data="Xhela6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضل ساتر 🎧", callback_data="Xhela7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وجع القلب 🎧", callback_data="Xhela8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني مسلم الحزين", reply_markup=keyboard)
    
########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^Xhela1 (\\d+)$"))
async def Xhela1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/100", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xhela2 (\\d+)$"))
async def Xhela2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/101", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xhela3 (\\d+)$"))
async def Xhela3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/102", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xhela4 (\\d+)$"))
async def Xhela4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/103", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xhela5 (\\d+)$"))
async def Xhela5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/104", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xhela6 (\\d+)$"))
async def Xhela6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/105", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xhela7 (\\d+)$"))
async def Xhela7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/106", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xhela8 (\\d+)$"))
async def Xhela8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/107", reply_to_message_id=mid)

########################################################################################################################
########################################################################################################################
@Client.on_callback_query(filters.regex("^pplal (\\d+)$"))
async def marwan(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("جوب 🎧", callback_data="Xmar1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مزاجنجي 🎧", callback_data="Xmar2 " + str(m.from_user.id))],
        [InlineKeyboardButton("عيد ميلاد 🎧", callback_data="Xmar3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("صنع في مصر 🎧", callback_data="Xmar4 " + str(m.from_user.id))],
        [InlineKeyboardButton("بشوف نفسي 🎧", callback_data="Xmar5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ممنوع الاقتراب 🎧", callback_data="Xmar6 " + str(m.from_user.id))],
        [InlineKeyboardButton("يفوت العمر 🎧", callback_data="Xmar9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حظر من الناس 🎧", callback_data="Xmar10 " + str(m.from_user.id))],
        [InlineKeyboardButton("سنين ضيعتها 🎧", callback_data="Xmar11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شاغلنا 🎧", callback_data="Xmar12 " + str(m.from_user.id))], 
        
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر ماتريد من قائمة اغاني مسلم مهرجانات\n√", reply_markup=keyboard)
########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^Xmar1 (\\d+)$"))
async def Xmar1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/86", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmar2 (\\d+)$"))
async def Xmar2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/87", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmar3 (\\d+)$"))
async def Xmar3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/88", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmar4 (\\d+)$"))
async def Xmar4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/89", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmar5 (\\d+)$"))
async def Xmar5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/90", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmar6 (\\d+)$"))
async def Xmar6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/91", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmar9 (\\d+)$"))
async def Xmar9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/95", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmar10 (\\d+)$"))
async def Xmar10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/96", reply_to_message_id=mid)

@Client.on_callback_query(filters.regex("^Xmar11 (\\d+)$"))
async def Xmar11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/97", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^Xmar12 (\\d+)$"))
async def Xmar12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/98", reply_to_message_id=mid)







########################################################################################################################
########################################################################################################################
###############################################
##  CopyRight & Creator File And Programing  ##
##                                           ##
##     #######  ######  #####*     *##*      ##
##     #  #  #  ###     #     *   *    *     ##
##     #     #  ##      #     *   *    *     ##
##     #     #  #####   #####*     *##*      ##
##                                           ##
###############################################


