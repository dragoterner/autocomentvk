import pyautogui as pg
from numpy import imag
import vk_captchasolver as vc
import pywinauto

while True:
    pg.screenshot(imageFilename='captcha.png', region = (606, 295, 150, 65)) #делаем скриншот. первые две координаты - начало картинки, вторые две - размеры картирнки
    captcha = vc.solve(image='captcha.png') #скармливаем сохраненную картинку библиотеке и засовываем решение в переменную captcha
    pg.click(659, 375) #кликаем по полю ввода (ибо оно не всегда может быть активно)
    pywinauto.keyboard.send_keys(captcha, pause=0.1) #ввод данных из нашей переменной в поле ввода капчи.
    pg.click(756, 432) #кликаем по кнопке отправить

while True:
    try:
        data = pg.locateOnScreen('coordinates.png', confidence=.8 ) #ищем поле ввода на экране. confidence - это то, для чего нам нужна была библиотека opencv - позволяет искать окно не со 100-процентным, а с 80-процентым совпадением. Быстрее чтоб искалось.
        if data != None: # другими словами - если поле ввода найдено, то делаем вещи.
            pg.screenshot(imageFilename='captcha.png', region = (606, 295, 150, 65))
            captcha = vc.solve(image='captcha.png')
            pg.click(659, 375)
            pywinauto.keyboard.send_keys(captcha, pause=0.1)
            pg.click(756, 432)
    except:
        pass