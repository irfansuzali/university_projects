# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uni_freelance_project.settings')

# import django
# django.setup()
# from posts.models import Category, Post 
# from users.models import CustomUser, School

# def populate():

#     users = [
#         {
#             "username": "ElonMusk",
#             "first_name": 'Elon',
#             "last_name": 'Musk',
#             'email': 'elonmusk@freelance.com',
#             'school': 'University of Illinois Urbana Champaign',
#             'year_in_school': 'Freshman',
#             'enrollment_year': 2020,
#             'graduation_year': 2020,
#             # 'password1': 'freelance123',
#             # 'password2': 'freelance123',
#         }
#     ]

#     schools = [
#         {
#             'name': 'University of Illinois Urbana Champaign'
#         },
#         {
#             'name': 'University of Illinois Springfield'
#         },
#         {
#             'name': 'University of Illinois Chicago'
#         }
#     ]
    
#     def add_school(name):
#         school = School.objects.get_or_create(name = name)[0]
#         school.save()
#         print('Added school - {0}'.format(name))

#     def add_user(user_object):
#         user = CustomUser.objects.get_or_create(
#             username = user_object['username'],
#             first_name = user_object['first_name'],
#             last_name = user_object['last_name'],
#             email = user_object['email'],
#             school = user_object['school'],
#             year_in_school = user_object['year_in_school'],
#             enrollment_year = user_object['enrollment_year'],
#             graduation_year = user_object['graduation_year'],
#             # password1 = user_object['password1'],
#             # password2 = user_object['password2']
#         )[0]
#         user.save()
#         print('Added user - {0}'.format(user_object['username']))
    
#     # for school in schools:
#     #     add_school(school['name'])
    
#     for user in users:
#         add_user(user)
    
    

# if __name__ == '__main__':
#     print('Starting Rango population script...')
#     populate()
