a = input("Введите номер телефона, пример: +79123456789:")
if a[:2] == "+7":
    print("Страна: Россия/Казахстан")
    if a[2] == "9":
        print("Телефон: Сотовый")
    else:
        print("Телефон: Стационарный")
    if a[:5] == "+7922" or a[:5] == "+7932":
        print("Оператор: МегаФон")
    elif a[:5] == "+7902" or a[:5] == "+7904":
        print("Оператор: МегаФон")
    elif a[:5] == "+7908" or a[:5] == "+7920":
        print("Оператор: МегаФон")
    elif a[:5] == "+7921" or a[:5] == "+7923":
        print("Оператор: МегаФон")
    elif a[:5] == "+7924" or a[:5] == "+7927":
        print("Оператор: МегаФон")
    elif a[:5] == "+7925" or a[:5] == "+7926":
        print("Оператор: МегаФон")
    elif a[:5] == "+7928" or a[:5] == "+7937":
        print("Оператор: МегаФон")
    elif a[:5] == "+7930" or a[:5] == "+7931":
        print("Оператор: МегаФон")
    elif a[:5] == "+7933" or a[:5] == "+7934":
        print("Оператор: МегаФон")
    elif a[:5] == "+7936" or a[:5] == "+7929":
        print("Оператор: МегаФон")
    elif a[:5] == "+7938" or a[:5] == "+7939":
        print("Оператор: МегаФон")
    elif a[:5] == "+7950" or a[:5] == "+7951":
        print("Оператор: МегаФон")
    elif a[:5] == "+7958" or a[:5] == "+7999":
        print("Оператор: МегаФон")
    elif a[:5] == "+7901" or a[:5] == "+7989":
        print("Оператор: МТС")
    elif a[:5] == "+7981" or a[:5] == "+7911":
        print("Оператор: МТС")
    elif a[:5] == "+7912" or a[:5] == "+7913":
        print("Оператор: МТС")
    elif a[:5] == "+7914" or a[:5] == "+7915":
        print("Оператор: МТС")
    elif a[:5] == "+7916" or a[:5] == "+7917":
        print("Оператор: МТС")
    elif a[:5] == "+7918" or a[:5] == "+7919":
        print("Оператор: МТС")
    elif a[:5] == "+7978" or a[:5] == "+7986":
        print("Оператор: МТС")
    elif a[:5] == "+7910" or a[:5] == "+7982":
        print("Оператор: МТС")
    elif a[:5] == "+7983" or a[:5] == "+7984":
        print("Оператор: МТС")
    elif a[:5] == "+7985" or a[:5] == "+7980":
        print("Оператор: МТС")
    elif a[:5] == "+7987" or a[:5] == "+7988":
        print("Оператор: МТС")
    elif a[:5] == "+7905" or a[:5] == "+7903":
        print("Оператор: Билайн")
    elif a[:5] == "+7909" or a[:5] == "+7906":
        print("Оператор: Билайн")
    elif a[:5] == "+7900" or a[:5] == "+7953":
        print("Оператор: Билайн")
    elif a[:5] == "+7960" or a[:5] == "+7961":
        print("Оператор: Билайн")
    elif a[:5] == "+7962" or a[:5] == "+7963":
        print("Оператор: Билайн")
    elif a[:5] == "+7964" or a[:5] == "+7965":
        print("Оператор: Билайн")
    elif a[:5] == "+7966" or a[:5] == "+7967":
        print("Оператор: Билайн")
    elif a[:5] == "+7968" or a[:5] == "+7969":
        print("Оператор: Билайн")
    elif a[:5] == "+7994":
        print("Оператор: Билайн")
    elif a[:5] == "+7993":
        print("Оператор: Тинькофф Мобайл")
    elif a[:5] == "+7995":
        print("Оператор: Тинькофф Мобайл")
    elif a[:5] == "+7997":
        print("Оператор: Мотив")
    elif a[:5] == "+7977":
        print("Оператор: Теле2")
    if a[:5] == "+7495" or a[:5] == "+7499":
        print("Город: Москва")
    elif a[:5] == "+7390":
        print("Город: Абакан")
        print("Регион: Республика Хакасия")
    elif a[:5] == "+7427":
        print("Город: Анадырь")
        print("Регион: Чукотский Автономный Округ")
    elif a[:5] == "+7818":
        print("Город: Архангельск")
        print("Регион: Архангельская область")
    elif a[:5] == "+7851":
        print("Город: Астрахань")
        print("Регион: Астраханская область")
    elif a[:5] == "+7385":
        print("Город: Барнаул")
        print("Регион: Алтайский край")
    elif a[:5] == "+7472":
        print("Город: Белгород")
        print("Регион: Белгородская область")
    elif a[:5] == "+7426":
        print("Город: Биробиджан")
        print("Регион: Еврейская Автономная область")
    elif a[:5] == "+7416":
        print("Город: Благовещенск")
        print("Регион: Амурская область")
    elif a[:5] == "+7483":
        print("Город: Брянск")
        print("Регион: Брянская область")
    elif a[:5] == "+7816":
        print("Город: Великий Новгород")
        print("Регион: Новгородская область")
    elif a[:5] == "+7426":
        print("Город: Владивосток")
        print("Регион: Приморский край")
    elif a[:5] == "+7867":
        print("Город: Владикавказ")
        print("Регион: Республика Северная Осетия")
    elif a[:5] == "+7492":
        print("Город: Владимир")
        print("Регион: Владимирская область")
    elif a[:5] == "+7844":
        print("Город: Волгоград")
        print("Регион: Волгоградская область")
    elif a[:5] == "+7817":
        print("Город: Вологда")
        print("Регион: Вологодская область")
    elif a[:5] == "+7473":
        print("Город: Воронеж")
        print("Регион: Воронежская область")
    elif a[:5] == "+7388":
        print("Город: Горно-Алтайск")
        print("Регион: Республика Алтай")
    elif a[:5] == "+7871":
        print("Город: Грозный")
        print("Регион: Чеченская Республика")
    elif a[:5] == "+7343":
        print("Город: Екатеринбург")
        print("Регион: Свердловская область")
    elif a[:5] == "+7493":
        print("Город: Иваново")
        print("Регион: Ивановская область")
    elif a[:5] == "+7341":
        print("Город: Ижевск")
        print("Регион: Удмуртская Республика")
    elif a[:5] == "+7395":
        print("Город: Иркутск")
        print("Регион: Иркутская область")
    elif a[:5] == "+7836":
        print("Город: Йошкар-Ола")
        print("Регион: Республика Марий Эл")
    elif a[:5] == "+7843":
        print("Город: Казань")
        print("Регион: Республика Татарстан")
    elif a[:5] == "+7401":
        print("Город: Калининград")
        print("Регион: Калининградская область")
    elif a[:5] == "+7484":
        print("Город: Калуга")
        print("Регион: Калужская область")
    elif a[:5] == "+7384":
        print("Город: Кемерово")
        print("Регион: Кемеровская область")
    elif a[:5] == "+7833":
        print("Город: Киров")
        print("Регион: Кировская область")
    elif a[:5] == "+7494":
        print("Город: Кострома")
        print("Регион: Костромская область")
    elif a[:5] == "+7861":
        print("Город: Краснодар")
        print("Регион: Краснодарский край")
    elif a[:5] == "+7391":
        print("Город: Красноярск")
        print("Регион: Красноярский край")
    elif a[:5] == "+7352":
        print("Город: Курган")
        print("Регион: Курганская область")
    elif a[:5] == "+7471":
        print("Город: Курск")
        print("Регион: Курская область")
    elif a[:5] == "+7394":
        print("Город: Кызыл")
        print("Регион: Республика Тыва")
    elif a[:5] == "+7474":
        print("Город: Липецк")
        print("Регион: Липецкая область")
    elif a[:5] == "+7413":
        print("Город: Магадан")
        print("Регион: Магаданская область")
    elif a[:5] == "+7877":
        print("Город: Майкоп")
        print("Регион: Республика Адыгея")
    elif a[:5] == "+7872":
        print("Город: Махачкала")
        print("Регион: Республика Дагестан")
    elif a[:5] == "+7815":
        print("Город: Мурманск")
        print("Регион: Мурманская область")
    elif a[:5] == "+7873":
        print("Город: Назрань")
        print("Регион: Республика Игнушетия")
    elif a[:5] == "+7866":
        print("Город: Нальчик")
        print("Регион: Кабардино-Балкарская Республика")
    elif a[:5] == "+7831":
        print("Город: Нижный Новгород")
        print("Регион: Нижегородская область")
    elif a[:5] == "+7350" or a[:5] == "+7383":
        print("Город: Новосибирск")
        print("Регион: Новосибирская область")
    elif a[:5] == "+7381":
        print("Город: Омск")
        print("Регион: Омская область")
    elif a[:5] == "+7353":
        print("Город: Оренбург")
        print("Регион: Оренбургская область")
    elif a[:5] == "+7841":
        print("Город: Пенза")
        print("Регион: Пензенская область")
    elif a[:5] == "+7342":
        print("Город: Пермь")
        print("Регион: Пермский край")
    elif a[:5] == "+7814":
        print("Город: Петрозаводск")
        print("Регион: Республика Карелия")
    elif a[:5] == "+7415":
        print("Город: Петропавловск-Камчатский")
        print("Регион: Камчатский край")
    elif a[:5] == "+7811":
        print("Город: Псков")
        print("Регион: Псковская область")
    elif a[:5] == "+7863":
        print("Город: Ростов-на-Дону")
        print("Регион: Ростовская область")
    elif a[:5] == "+7491":
        print("Город: Рязань")
        print("Регион: Рязанская область")
    elif a[:5] == "+7349":
        print("Город: Салехард")
        print("Регион: Ямало-Ненецкий Автономный Округ")
    elif a[:5] == "+7846":
        print("Город: Самара")
        print("Регион: Самарская область")
    elif a[:5] == "+7812":
        print("Город: Санкт-Петербург")
    elif a[:5] == "+7834":
        print("Город: Саранск")
        print("Регион: Республика Мордовия")
    elif a[:5] == "+7845":
        print("Город: Саратов")
        print("Регион: Саратовская область")
    elif a[:5] == "+7481":
        print("Город: Смоленск")
        print("Регион: Смоленская область")
    elif a[:5] == "+7862":
        print("Город: Сочи")
        print("Регион: Краснодарский край")
    elif a[:5] == "+7865":
        print("Город: Ставрополь")
        print("Регион: Ставропольский край")
    elif a[:5] == "+7346":
        print("Город: Сургут")
        print("Регион: Ханты-Манскийский Автономный Округ")
    elif a[:5] == "+7821":
        print("Город: Сыктывкар")
        print("Регион: Республика Коми")
    elif a[:5] == "+7475":
        print("Город: Тамбов")
        print("Регион: Тамбовская область")
    elif a[:5] == "+7482":
        print("Город: Тверь")
        print("Регион: Тверская область")
    elif a[:5] == "+7848":
        print("Город: Тольятти")
        print("Регион: Самарская область")
    elif a[:5] == "+7382":
        print("Город: Томск")
        print("Регион: Томская область")
    elif a[:5] == "+7487":
        print("Город: Тула")
        print("Регион: Тульская область")
    elif a[:5] == "+7345":
        print("Город: Тюмень")
        print("Регион: Тюменская область")
    elif a[:5] == "+7301":
        print("Город: Улан-Удэ")
        print("Регион: Республика Бурятия")
    elif a[:5] == "+7842":
        print("Город: Ульяновск")
        print("Регион: Ульяновская область")
    elif a[:5] == "+7347":
        print("Город: Уфа")
        print("Регион: Республика Башкортостан")
    elif a[:5] == "+7421":
        print("Город: Хабаровск")
        print("Регион: Хабаровский край")
    elif a[:5] == "+7835":
        print("Город: Чебоксары")
        print("Регион: Республика Чувашия")
    elif a[:5] == "+7351":
        print("Город: Челябинск")
        print("Регион: Челябинская область")
    elif a[:5] == "+7820":
        print("Город: Череповец")
        print("Регион: Вологодская область")
    elif a[:5] == "+7878":
        print("Город: Черкесск")
        print("Регион: Республика Карачаево-Черкесия")
    elif a[:5] == "+7302":
        print("Город: Чита")
        print("Регион: Забайкальский край")
    elif a[:5] == "+7847":
        print("Город: Элиста")
        print("Регион: Республика Калмыкия")
    elif a[:5] == "+7424":
        print("Город: Южно-Сахалинск")
        print("Регион: Сахалинская область")
    elif a[:5] == "+7411":
        print("Город: Якутск")
        print("Регион: Республика Саха (Якутия)")
    elif a[:5] == "+7485":
        print("Город: Ярославль")
        print("Регион: Ярославкая область")
elif a[:2] == "+1":
    print("Страна: США/Канада")
elif a[:3] == "+90":
    print("Страна: Турция")
elif a[:4] == "+976":
    print("Страна: Монголия")
elif a[:4] == "+850":
    print("Страна: КНДР")
elif a[:3] == "+82":
    print("Страна: Южная корея")
elif a[:3] == "+86":
    print("Страна: Китай")
elif a[:3] == "+61":
    print("Страна: Австралия")
elif a[:3] == "+64":
    print("Страна: Новая Зеландия")
elif a[:3] == "+81":
    print("Страна: Япония")
elif a[:3] == "+49":
    print("Страна: Германия")
elif a[:3] == "+39":
    print("Страна: Италия/Ватикан")
elif a[:3] == "+44":
    print("Страна: Великобритания")
elif a[:3] == "+43":
    print("Страна: Австрия")
elif a[:3] == "+32":
    print("Страна: Бельгия")
elif a[:4] == "+359":
    print("Страна: Болгария")
elif a[:4] == "+994":
    print("Страна: Азербайджан")
elif a[:4] == "+355":
    print("Страна: Албания")
elif a[:3] == "+36":
    print("Страна: Венгрия")
elif a[:3] == "+30":
    print("Страна: Греция")
elif a[:3] == "+45":
    print("Страна: Дания")
elif a[:4] == "+299":
    print("Страна: Гренландия")
elif a[:4] == "+353":
    print("Страна: Ирландия")
elif a[:4] == "+886":
    print("Страна: Тайвань (Китай)")
elif a[:3] == "+34":
    print("Страна: Испания")
elif a[:4] == "+357":
    print("Страна: Кипр")
elif a[:4] == "+371":
    print("Страна: Латвия")
elif a[:4] == "+370":
    print("Страна: Литва")
elif a[:4] == "+352":
    print("Страна: Люксембург")
elif a[:4] == "+356":
    print("Страна: Мальта")
elif a[:3] == "+31":
    print("Страна: Нидерланды")
elif a[:3] == "+48":
    print("Страна: Польша")
elif a[:4] == "+351":
    print("Страна: Португалия")
elif a[:3] == "+40":
    print("Страна: Румыния")
elif a[:4] == "+421":
    print("Страна: Словакия")
elif a[:4] == "+386":
    print("Страна: Словения")
elif a[:4] == "+358":
    print("Страна: Финляндия")
elif a[:3] == "+33":
    print("Страна: Франция")
elif a[:4] == "+385":
    print("Страна: Хорватия")
elif a[:4] == "+420":
    print("Страна: Чехия")
elif a[:3] == "+46":
    print("Страна: Швеция")
elif a[:4] == "+372":
    print("Страна: Эстония")
elif a[:3] == "+41":
    print("Страна: Швейцария")
elif a[:4] == "+375":
    print("Страна: Беларусь")
elif a[:4] == "+354":
    print("Страна: Исландия")
elif a[:4] == "+379":
    print("Страна: Ватикан")
elif a[:3] == "+94":
    print("Страна: Шри-Ланка")
elif a[:4] == "+960":
    print("Страна: Мальдивы")
elif a[:3] == "+91":
    print("Страна: Индия")
elif a[:4] == "+387":
    print("Страна: Босния и Герцеговина")
elif a[:4] == "+373":
    print("Страна: Молдова")
elif a[:4] == "+505":
    print("Страна: Никарагуа")
elif a[:3] == "+58":
    print("Страна: Венесуэла")
elif a[:4] == "+674":
    print("Страна: Науру")
elif a[:4] == "+963":
    print("Страна: Сирия")
elif a[:3] == "+56":
    print("Страна: Чили")
elif a[:4] == "+593":
    print("Страна: Эквадор")
elif a[:3] == "+55":
    print("Страна: Бразилия")
elif a[:3] == "+27":
    print("Страна: ЮАР")
elif a[:3] == "+98":
    print("Страна: Иран")
elif a[:4] == "+964":
    print("Страна: Ирак")
elif a[:3] == "+54":
    print("Страна: Аргентина")
elif a[:4] == "+213":
    print("Страна: Алжир")
elif a[:4] == "+382":
    print("Страна: Черногория")
elif a[:4] == "+389":
    print("Страна: Северная Македония")
elif a[:4] == "+381":
    print("Страна: Сербия")
elif a[:4] == "+380":
    print("Страна: Украина")
elif a[:4] == "+374":
    print("Страна: Армения")
elif a[:4] == "+597":
    print("Страна: Суринам")
elif a[:4] == "+592":
    print("Страна: Гайана")
elif a[:3] == "+57":
    print("Страна: Колумбия")
elif a[:3] == "+51":
    print("Страна: Перу")
elif a[:4] == "+591":
    print("Страна: Боливия")
elif a[:4] == "+595":
    print("Страна: Парагвай")
elif a[:4] == "+598":
    print("Страна: Уругвай")
elif a[:4] == "+376":
    print("Страна: Андорра")
elif a[:4] == "+679":
    print("Страна: Фиджи")
elif a[:4] == "+249":
    print("Страна: Судан")
elif a[:4] == "+211":
    print("Страна: Южный Судан")
elif a[:4] == "+232":
    print("Страна: Сьерра-Леоне")
elif a[:4] == "+263":
    print("Страна: Зибавбве")
elif a[:4] == "+260":
    print("Страна: Замбия")
elif a[:4] == "+264":
    print("Страна: Намибия")
elif a[:4] == "+967":
    print("Страна: Йемен")
elif a[:3] == "+60":
    print("Страна: Малайзия")
elif a[:4] == "+880":
    print("Страна: Бангладеш")
elif a[:3] == "+65":
    print("Страна: Сингапур")
elif a[:4] == "+238":
    print("Страна: Кабо-Верде")
elif a[:3] == "+20":
    print("Страна: Египет")
elif a[:4] == "+504":
    print("Страна: Гондурас")
elif a[:4] == "+977":
    print("Страна: Непал")
elif a[:4] == "+855":
    print("Страна: Камбоджа")
elif a[:3] == "+95":
    print("Страна: Мьянма")
elif a[:4] == "+975":
    print("Страна: Бутан")
elif a[:4] == "+993":
    print("Страна: Туркмения")
elif a[:4] == "+686":
    print("Страна: Кирибати")
elif a[:4] == "+691":
    print("Страна: Федеративные Штаты Микронезии")
elif a[:4] == "+688":
    print("Страна: Тувалу")
elif a[:4] == "+690":
    print("Страна: Токелау")
elif a[:4] == "+685":
    print("Страна: Самоа")
elif a[:4] == "+680":
    print("Страна: Палау")
elif a[:4] == "+683":
    print("Страна: Ниуэ")
elif a[:4] == "+682":
    print("Страна: Острова Кука")
elif a[:4] == "+678":
    print("Страна: Вануату")
elif a[:4] == "+687":
    print("Страна: Новая Каледония")
elif a[:4] == "+676":
    print("Страна: Тонга")
elif a[:4] == "+222":
    print("Страна: Мавритания")
elif a[:4] == "+223":
    print("Страна: Мали")
elif a[:4] == "+227":
    print("Страна: Нигер")
elif a[:4] == "+234":
    print("Страна: Нигерия")
elif a[:4] == "+235":
    print("Страна: Чад")
elif a[:4] == "+251":
    print("Страна: Эфиопия")
elif a[:4] == "+252":
    print("Страна: Сомали")
elif a[:4] == "+254":
    print("Страна: Кения")
elif a[:4] == "+377":
    print("Страна: Монако")
elif a[:3] == "+92":
    print("Страна: Пакистан")
elif a[:3] == "+93":
    print("Страна: Афганистан")
elif a[:4] == "+961":
    print("Страна: Ливан")
elif a[:4] == "+962":
    print("Страна: Иордания")
elif a[:4] == "+965":
    print("Страна: Кувейт")
elif a[:4] == "+966":
    print("Страна: Саудовская Аравия")
elif a[:4] == "+968":
    print("Страна: Оман")
elif a[:4] == "+971":
    print("Страна: ОАЭ")
elif a[:4] == "+972":
    print("Страна: Израиль")
elif a[:4] == "+973":
    print("Страна: Бахрейн")
elif a[:4] == "+974":
    print("Страна: Катар")
elif a[:4] == "+992":
    print("Страна: Таджикистан")
elif a[:4] == "+995":
    print("Страна: Грузия")
elif a[:4] == "+996":
    print("Страна: Киргизия")
elif a[:4] == "+998":
    print("Страна: Узбекистан")
elif a[:4] == "+383":
    print("Страна: Косово (Сербия)")
elif a[:4] == "+501":
    print("Страна: Белиз")
elif a[:3] == "+84":
    print("Страна: Вьетнам")
elif a[:4] == "+852":
    print("Страна: Гонконг")
elif a[:4] == "+853":
    print("Страна: Макао")
elif a[:4] == "+856":
    print("Страна: Лаос")
elif a[:3] == "+62":
    print("Страна: Индонезия")
elif a[:3] == "+63":
    print("Страна: Филиппины")
elif a[:3] == "+66":
    print("Страна: Таиланд")
elif a[:4] == "+670":
    print("Страна: Восточный Тимор")
elif a[:4] == "+673":
    print("Страна: Бруней")
elif a[:4] == "+675":
    print("Страна: Папуа - Новая Гвинея")
elif a[:4] == "+677":
    print("Страна: Соломоновы Острова")
elif a[:4] == "+681":
    print("Страна: Уоллис и Футуна")
elif a[:4] == "+692":
    print("Страна: Маршалловы Острова")
elif a[:4] == "+423":
    print("Страна: Лихтенштейн")
elif a[:3] == "+47":
    print("Страна: Норвегия")
elif a[:4] == "+500":
    print("Страна: Фолклендские Острова")
elif a[:4] == "+502":
    print("Страна: Гватемала")
elif a[:4] == "+503":
    print("Страна: Сальвадор")
elif a[:4] == "+506":
    print("Страна: Коста-Рика")
elif a[:4] == "+507":
    print("Страна: Панама")
elif a[:4] == "+508":
    print("Страна: Сен-Пьер и Микелон")
elif a[:4] == "+509":
    print("Страна: Гаити")
elif a[:3] == "+52":
    print("Страна: Мексика")
elif a[:3] == "+53":
    print("Страна: Куба")
elif a[:4] == "+378":
    print("Страна: Сан-Марино")
elif a[:4] == "+212":
    print("Страна: Марокко")
elif a[:4] == "+216":
    print("Страна: Тунис")
elif a[:4] == "+218":
    print("Страна: Ливия")
elif a[:4] == "+220":
    print("Страна: Гамбия")
elif a[:4] == "+221":
    print("Страна: Сенегал")
elif a[:4] == "+224":
    print("Страна: Гвинея")
elif a[:4] == "+291":
    print("Страна: Эритрея")
elif a[:4] == "+225":
    print("Страна: Кот-дИвуар")
elif a[:4] == "+226":
    print("Страна: Буркина-Фасо")
elif a[:4] == "+228":
    print("Страна: Того")
elif a[:4] == "+229":
    print("Страна: Бенин")
elif a[:4] == "+230":
    print("Страна: Маврикий")
elif a[:4] == "+231":
    print("Страна: Либерия")
elif a[:4] == "+233":
    print("Страна: Гана")
elif a[:4] == "+236":
    print("Страна: ЦАР")
elif a[:4] == "+237":
    print("Страна: Камерун")
elif a[:4] == "+239":
    print("Страна: Сан-Томе и Принсипи")
elif a[:4] == "+240":
    print("Страна: Экваториальная Гвинея")
elif a[:4] == "+241":
    print("Страна: Габон")
elif a[:4] == "+242":
    print("Страна: Республика Конго")
elif a[:4] == "+243":
    print("Страна: ДР Конго")
elif a[:4] == "+244":
    print("Страна: Ангола")
elif a[:4] == "+245":
    print("Страна: Гвинея-Бисау")
elif a[:4] == "+246":
    print("Страна: Британская Территория в Индийском Океане")
elif a[:4] == "+248":
    print("Страна: Сейшельские Острова")
print("Общая длина номера:", len(a))
print("WhatsApp:", "wa.me/" + a)
print("Telegram:", "t.me/" + a)
print("Viber:", "viber.click/" + a[1:])
print("Facebook Messenger:", "m.me/" + a[1:])
print("Возможные имена:", "gogtc.co/search/" + a[1:])