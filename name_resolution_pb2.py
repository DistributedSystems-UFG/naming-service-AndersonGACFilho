# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: name_resolution.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15name_resolution.proto\"5\n\x0bServiceInfo\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\"#\n\x0bServiceName\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\"\x1c\n\x08\x45ndpoint\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\"\x1c\n\x08Services\x12\x10\n\x08services\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"\x19\n\x06Result\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9d\x01\n\x0eNameResolution\x12!\n\x08Register\x12\x0c.ServiceInfo\x1a\x07.Result\x12!\n\x06Lookup\x12\x0c.ServiceName\x1a\t.Endpoint\x12#\n\nUnregister\x12\x0c.ServiceName\x1a\x07.Result\x12 \n\x0b\x41llServices\x12\x06.Empty\x1a\t.Servicesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'name_resolution_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SERVICEINFO']._serialized_start=25
  _globals['_SERVICEINFO']._serialized_end=78
  _globals['_SERVICENAME']._serialized_start=80
  _globals['_SERVICENAME']._serialized_end=115
  _globals['_ENDPOINT']._serialized_start=117
  _globals['_ENDPOINT']._serialized_end=145
  _globals['_SERVICES']._serialized_start=147
  _globals['_SERVICES']._serialized_end=175
  _globals['_EMPTY']._serialized_start=177
  _globals['_EMPTY']._serialized_end=184
  _globals['_RESULT']._serialized_start=186
  _globals['_RESULT']._serialized_end=211
  _globals['_NAMERESOLUTION']._serialized_start=214
  _globals['_NAMERESOLUTION']._serialized_end=371
# @@protoc_insertion_point(module_scope)