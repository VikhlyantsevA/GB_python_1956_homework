1. В задании 9.3 защищенные атрибуты не наследуются? А если этот атрибут у прародителя так сказать? Их всегда так неудобно вытаскивать или есть более элегантные методы?


2. В задании 9.5 постарался избежать копипаста при создании дочерних классов `Pen`, `Pencil` и `Handle` с перегрузкой метода `draw`, используя множественное наследование и вызов метода конкретного родителя через точечную нотацию. 

    Не уверен что это хороший вариант. Если есть лучшая практика, был бы благодарен за ссылку на нее.

    Повторяющаяся строка в дочерних классах:
    ```(python)
    print(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')
    ```