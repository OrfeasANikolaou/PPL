from faker import Faker


fake = Faker("en_US")
Faker.seed(12341)

 #   print(f"{fake.name()};{fake.address()}")
 #   print(f"{fake.name()};{modify_fake_addr(fake.address())}")
f = open("fake100.txt", "w")
for i in range(100):
    t_name = fake.name()
    t_addr = fake.address()
    t_addr = t_addr.replace("\n", ", ")
    t_dob  = fake.date_between(start_date='-90y', end_date='-18y')
    f.write(f"{t_name};{t_addr};{t_dob}\n")
