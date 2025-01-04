class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("คิวว่าง")
        else:
            print(f"ลูกค้าที่รอคิว: {self.items}")
    
    def peek_first(self):
        if not self.is_empty():
            return self.items[0]
        return None


class HairSalonQueue:
    def __init__(self):
        self.waiting_queue = Queue()
        self.service_times = {
            "ตัดผม": 30,   # เวลารอสำหรับตัดผม 30 นาที
            "สระ": 20,     # เวลารอสำหรับสระผม 20 นาที
            "ย้อมสี": 60   # เวลารอสำหรับย้อมสี 60 นาที
        }
    
    def add_customer(self, name, service_type):
        # เพิ่มลูกค้าเข้าไปในคิวพร้อมบริการ
        if service_type in self.service_times:
            self.waiting_queue.enqueue({"name": name, "service": service_type})
            print(f"ลูกค้า {name} เข้าคิวสำหรับบริการ: {service_type}")
        else:
            print(f"บริการ {service_type} ไม่มีในรายการบริการ")
    
    def serve_customer(self):
        # เรียกลูกค้าคนถัดไป
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer['name']} สำหรับบริการ: {customer['service']}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def show_waiting_queue(self):
        # แสดงลูกค้าที่รอในคิว
        print(f"จำนวนลูกค้าที่รอคิว: {self.waiting_queue.size()}")
        self.waiting_queue.display()
    
    def estimate_wait_time(self):
        # คำนวณเวลารอโดยประมาณ
        if not self.waiting_queue.is_empty():
            total_wait_time = 0
            for customer in self.waiting_queue.items:
                total_wait_time += self.service_times[customer['service']]
            print(f"เวลารอโดยประมาณ: {total_wait_time} นาที")
        else:
            print("ไม่มีลูกค้าในคิว")


# สร้างร้านตัดผม
salon = HairSalonQueue()

# เพิ่มลูกค้าเข้าคิว
salon.add_customer("กันตพัฒน์", "ตัดผม")
salon.add_customer("คิมมินแจ", "สระ")
salon.add_customer("จิรสิน", "ย้อมสี")

# แสดงจำนวนลูกค้าที่รอและรายการลูกค้า
salon.show_waiting_queue()

# แสดงเวลารอโดยประมาณ
salon.estimate_wait_time()

# เรียกลูกค้าคนถัดไป
salon.serve_customer()

# แสดงจำนวนลูกค้าที่รอหลังจากเรียกลูกค้า
salon.show_waiting_queue()

# แสดงเวลารอโดยประมาณหลังจากเรียกลูกค้า
salon.estimate_wait_time()

# เรียกลูกค้าต่อไป
salon.serve_customer()

# แสดงจำนวนลูกค้าที่รอหลังจากเสิร์ฟ
salon.show_waiting_queue()
salon.estimate_wait_time()

# เรียกลูกค้าทั้งหมด
salon.serve_customer()
salon.show_waiting_queue()
salon.estimate_wait_time()
