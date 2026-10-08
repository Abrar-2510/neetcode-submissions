class Node:
    def __init__(self, val=0):
        self.val = val  # القيمة المخزنة في العقدة
        self.next = None  # الرابط إلى العقدة التالية

class LinkedList:
    def __init__(self):
        self.head = None  # الرأس يبدأ فارغًا

    def get(self, i: int) -> int:
        current = self.head
        index = 0
        while current:
            if index == i:  # إذا وصلنا إلى الفهرس المطلوب
                return current.val
            current = current.next
            index += 1
        return -1  # إذا كان الفهرس خارج الحدود

    def insertHead(self, val: int) -> None:
        new_node = Node(val)  # إنشاء عقدة جديدة
        new_node.next = self.head  # ربط العقدة الجديدة بالرأس الحالي
        self.head = new_node  # تعيين الرأس ليصبح العقدة الجديدة

    def insertTail(self, val: int) -> None:
        new_node = Node(val)  # إنشاء عقدة جديدة
        if not self.head:  # إذا كانت القائمة فارغة
            self.head = new_node  # تعيين الرأس ليكون العقدة الجديدة
            return
        current = self.head
        while current.next:  # المرور حتى العقدة الأخيرة
            current = current.next
        current.next = new_node  # ربط العقدة الجديدة في النهاية

    def remove(self, i: int) -> bool:
        if not self.head:  # إذا كانت القائمة فارغة
            return False
        if i == 0:  # إذا كان الفهرس هو الرأس
            self.head = self.head.next  # تغيير الرأس ليكون العقدة التالية
            return True
        current = self.head
        index = 0
        while current and current.next:
            if index == i - 1:  # إذا كانت هذه العقدة هي التي تسبق العقدة المراد حذفها
                current.next = current.next.next  # ربط العقدة التي تسبق العقدة المحذوفة بالعقدة التي تليها
                return True
            current = current.next
            index += 1
        return False  # إذا كان الفهرس خارج الحدود

    def getValues(self) -> list:
        values = []
        current = self.head
        while current:
            values.append(current.val)  # إضافة القيمة إلى المصفوفة
            current = current.next
        return values  # إرجاع المصفوفة التي تحتوي على جميع القيم
