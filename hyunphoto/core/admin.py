# from django.apps import apps
# from django.contrib import admin
# from django.http import JsonResponse
# from django.utils.text import capfirst
# from django.urls import NoReverseMatch, reverse
# from django.core.exceptions import ValidationError
# from django.shortcuts import get_object_or_404
# import json
# import django.contrib.auth as auth

# from photos.models import Photo, Price


# class CustomAdminBase(admin.ModelAdmin):
#     # print(apps.get_models(), len(apps.get_models()))
#     extra_field_mapping = {}
#     foreign_key_fields = {}
#     boolean_fields = []
#     required_fields = []

#     def get_field_headers(self, queryset):
#         print('Model Name:::', queryset.model._meta)
#         return [field.name for field in queryset.model._meta.fields]

#     def map_extra_fields(self, data_dict):
#         for key, value in self.extra_field_mapping.items():
#             data_dict[key] = data_dict.get(value)
#         return data_dict

#     def process_field(self, field_name, value):
#         if field_name in self.foreign_key_fields:
#             model = self.foreign_key_fields[field_name]
#             return get_object_or_404(model, id=value)
#         elif field_name in self.boolean_fields:
#             if value == '1':
#                 return True
#             elif value == '0':
#                 return False
#             else:
#                 return ValueError(f'{field_name} 값은 true 혹은 false 중 하나여야 합니다.')
#         else:
#             return value

#     def handle_deleted_data(self, deleted_data):
#         for row_id in deleted_data:
#             data = self.model.objects.get(id=row_id)
#             data.delete()

#     def handle_inserted_data(self, headers, inserted_data):
#         # print('====handle inerted data function===')
#         for row in inserted_data:
#             if list(set(row[1:]))[0]=='None':
#                 continue
#             # print('!!!!', set(row))
#             # print(row)
#             # print('--------')

#             data_dict = dict(zip(headers[1:], row[1:]))
#             data_dict = self.map_extra_fields(data_dict)

#             for field_name, value in data_dict.items():
#                 # print('------', type(data_dict[field_name]))
#                 if field_name in self.required_fields and not data_dict[field_name]:
#                     raise Exception(field_name + '은 필수값입니다.')
#                 data_dict[field_name] = self.process_field(field_name, value)

#             self.model.objects.create(**data_dict)

#     def handle_changed_data(self, changed_data):
#         # print('change', changed_data)
#         try:
#             for row in changed_data:
#                 instance = get_object_or_404(self.model, id=row[0])

#                 processed_value = self.process_field(row[1], row[3])
#                 setattr(instance, row[1], processed_value)
#                 instance.save()
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

#     def changelist_view(self, request, extra_context=None):
#         queryset = self.get_queryset(request)
#         headers = self.get_field_headers(queryset)
#         data = list(queryset.values(*headers))

#         for row in data:
#             for field_name in row:
#                 if field_name in self.boolean_fields:
#                     row[field_name] = 1 if row[field_name] == True else 0
#         # print('data', data)

#         if request.method == 'GET':
#             response = super().changelist_view(request)

#             response.context_data['table_data'] = {'header': headers, 'body': data}
#             # print('data::::',data)
#             return response
#         elif request.method == 'POST':
#             try:
#                 load_request = json.loads(request.body)
#                 action = load_request.get('action')
#                 # print(load_request)

#                 if action == 'load':
#                     return JsonResponse({'status': 'success', 'data': data}, status=200)

#                 elif action == 'save':
#                     changed_data = load_request.get('changedData', [])
#                     inserted_data = load_request.get('insertedData', [])
#                     deleted_data = load_request.get('deletedData', [])

#                     if not changed_data and not inserted_data and not deleted_data:
#                         return JsonResponse({'status': 'error', 'message': '변경사항이 없습니다.'}, status=400)

#                     if deleted_data:
#                         try:
#                             self.handle_deleted_data(deleted_data)
#                         except Exception as e:
#                             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

#                     if inserted_data:
#                         try:
#                             print('changelist_view inserted_data', inserted_data)
#                             self.handle_inserted_data(headers, inserted_data)
#                         except ValidationError as e:
#                             print('handle_inserted_data validationerror:', e)
#                             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
#                         except Exception as e:
#                             print('handle_inserted_data error:', e)
#                             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
#                     else:
#                         print('non-inserted_data')

#                     if changed_data:
#                         try:
#                             self.handle_changed_data(changed_data)
#                         except Exception as e:
#                             print('handle_changed_data error:', e)
#                             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

#                     data = list(self.get_queryset(request).values(*headers))
#                     for row in data:
#                         for field_name in row:
#                             if field_name in self.boolean_fields:
#                                 row[field_name] = 1 if row[field_name] == True else 0
#                     return JsonResponse({'data': data, 'status': 'success',
#                                          'message': '변경사항이 저장되었습니다.'}, status=200)
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


# admin.site.register(Photo, CustomAdminBase)