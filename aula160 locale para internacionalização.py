# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
print(calendar.calendar(2330))
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
print(calendar.calendar(2330))
locale.setlocale(locale.LC_ALL, 'hu_HU.UTF-8')
print(calendar.calendar(2330))
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print(calendar.calendar(2330))