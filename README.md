# done list

1 задание:
	Сделан генератор символов(символов 4, латиница верхнего и нижнего регистра + цифры)
		1)Уникальность можно сделать с помощью 
				def check(value):
    				if not value.name.endswith('.jpg', '.bmp', '.png', '.tiff'):
        				raise Error('"Некорректный формат файла, поддерживаемые форматы: JPG, BMP, PNG, TIFF')

2 задание:
	Сделан сервис обратной связи:
		1)Пользователь может оставить сообщение, при этом сохранив копию сообщения на своем почтовом ящике
		2)Не доделана функция прикрепления файлов(изображений), возникает ошибка (module 'django.http.request' has no attribute 'FILES') (см. комментарии в views.py)
		3)Определение размера файла можно сделать с помощью FieldFile.size и простого if
		4)Не сделано обращение в обратную связь для авторизованных пользователей.
		5)В settings.py стоит EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
		данные направляются не на почту, а в консоль django для проверки отправляемых данных
