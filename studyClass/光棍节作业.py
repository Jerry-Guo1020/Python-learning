# 第一题
def greet(name):
    print("Hello,"+ name)

greet("Bob")
greet("Alice")

# 第二题
def describe_animal(name, animal_type='dog'):
    print(f'\nI have a {animal_type} named {name}.')

describe_animal(name="Willie")
describe_animal("Harry", "cat")
describe_animal(animal_type="hamster",name="Fuzzy")

# 第三题
def build_car(brand, model, **car_info):
    car = {
        'brand':brand,
        'model':model
    }
    car.update(car_info)
    return car

dict = build_car('tesla', 'model S', color ='red', fsd = True)
print("车辆信息：", dict)


# 第四题
def remove_duplicates(lst):
    # seen = set()
    # result = []
    # for item in lst:
    #     if item not in seen:
    #         seen.add(item)
    #         result.append(item)
    # return result 

    return list(set(lst))

origin_list = [1, 2, 3, 4, 5, 4, 2, 9, 1, 10]
then_list = remove_duplicates(origin_list)
print("原始列表：", origin_list)
print("去除列表：", then_list)
print("原列表是否被修改：" ,origin_list == [1, 2, 3, 4, 5, 4, 2, 9, 1, 10])



# 第五题
def make_sandwich(*ingredients):
    print("\n--- 开始制作您的三明治 ---")
    if ingredients:
        print("您选择的配料包括:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
        print("三明治制作完成！祝您用餐愉快！")
    else:
        print("您没有选择任何配料，我们无法为您制作一个空三明治。")



make_sandwich('火腿', '奶酪', '生菜')
# make_sandwich('金枪鱼', '沙拉酱')
# make_sandwich('培根')
make_sandwich()

# 第六题


