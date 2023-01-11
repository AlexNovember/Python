

@bot.message_handler(content_types=['document'])
# def answer(msg: types.Message):
#     filename = msg.document.file_name
#     with open(filename, 'wb') as file:
#         file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
#     bot.send_message(chat_id=msg.from_user.id, text='Loading')