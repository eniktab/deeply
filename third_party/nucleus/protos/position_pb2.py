# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: position.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='position.proto',
  package='nucleus.genomics.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eposition.proto\x12\x13nucleus.genomics.v1\"L\n\x08Position\x12\x16\n\x0ereference_name\x18\x01 \x01(\t\x12\x10\n\x08position\x18\x02 \x01(\x03\x12\x16\n\x0ereverse_strand\x18\x03 \x01(\x08\x62\x06proto3'
)




_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='nucleus.genomics.v1.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='nucleus.genomics.v1.Position.reference_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='nucleus.genomics.v1.Position.position', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reverse_strand', full_name='nucleus.genomics.v1.Position.reverse_strand', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['Position'] = _POSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'position_pb2'
  # @@protoc_insertion_point(class_scope:nucleus.genomics.v1.Position)
  })
_sym_db.RegisterMessage(Position)


# @@protoc_insertion_point(module_scope)
