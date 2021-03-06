# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='users.proto',
  package='users',
  syntax='proto3',
  serialized_pb=_b('\n\x0busers.proto\x12\x05users\"\x1d\n\x0cUsersRequest\x12\r\n\x05match\x18\x01 \x01(\t\"7\n\nUsersReply\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x1a\n\x05users\x18\x02 \x03(\x0b\x32\x0b.users.User\"\xd3\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\r\n\x05phone\x18\x04 \x01(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x06 \x01(\x08\x12\x0b\n\x03lat\x18\x07 \x01(\x02\x12\x0b\n\x03lng\x18\x08 \x01(\x02\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x1f\n\x07\x63ountry\x18\n \x01(\x0b\x32\x0e.users.Country\x12 \n\x08payments\x18\x0b \x03(\x0b\x32\x0e.users.Payment\"7\n\x07\x43ountry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\"*\n\x07Payment\x12\x0f\n\x07\x63reated\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x32r\n\x05Users\x12/\n\x03get\x12\x13.users.UsersRequest\x1a\x11.users.UsersReply\"\x00\x12\x38\n\nget_stream\x12\x13.users.UsersRequest\x1a\x11.users.UsersReply\"\x00\x30\x01\x62\x06proto3')
)




_USERSREQUEST = _descriptor.Descriptor(
  name='UsersRequest',
  full_name='users.UsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='users.UsersRequest.match', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=51,
)


_USERSREPLY = _descriptor.Descriptor(
  name='UsersReply',
  full_name='users.UsersReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='users.UsersReply.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='users', full_name='users.UsersReply.users', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=108,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='users.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='users.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surname', full_name='users.User.surname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='users.User.phone', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='users.User.created', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active', full_name='users.User.active', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='users.User.lat', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lng', full_name='users.User.lng', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='users.User.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='users.User.country', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payments', full_name='users.User.payments', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=322,
)


_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='users.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='users.Country.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency', full_name='users.Country.currency', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='users.Country.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=379,
)


_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='users.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='users.Payment.created', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='users.Payment.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=381,
  serialized_end=423,
)

_USERSREPLY.fields_by_name['users'].message_type = _USER
_USER.fields_by_name['country'].message_type = _COUNTRY
_USER.fields_by_name['payments'].message_type = _PAYMENT
DESCRIPTOR.message_types_by_name['UsersRequest'] = _USERSREQUEST
DESCRIPTOR.message_types_by_name['UsersReply'] = _USERSREPLY
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
DESCRIPTOR.message_types_by_name['Payment'] = _PAYMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UsersRequest = _reflection.GeneratedProtocolMessageType('UsersRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERSREQUEST,
  __module__ = 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UsersRequest)
  ))
_sym_db.RegisterMessage(UsersRequest)

UsersReply = _reflection.GeneratedProtocolMessageType('UsersReply', (_message.Message,), dict(
  DESCRIPTOR = _USERSREPLY,
  __module__ = 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UsersReply)
  ))
_sym_db.RegisterMessage(UsersReply)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.User)
  ))
_sym_db.RegisterMessage(User)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), dict(
  DESCRIPTOR = _COUNTRY,
  __module__ = 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.Country)
  ))
_sym_db.RegisterMessage(Country)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENT,
  __module__ = 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.Payment)
  ))
_sym_db.RegisterMessage(Payment)



_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='users.Users',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=425,
  serialized_end=539,
  methods=[
  _descriptor.MethodDescriptor(
    name='get',
    full_name='users.Users.get',
    index=0,
    containing_service=None,
    input_type=_USERSREQUEST,
    output_type=_USERSREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_stream',
    full_name='users.Users.get_stream',
    index=1,
    containing_service=None,
    input_type=_USERSREQUEST,
    output_type=_USERSREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class UsersStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.get = channel.unary_unary(
          '/users.Users/get',
          request_serializer=UsersRequest.SerializeToString,
          response_deserializer=UsersReply.FromString,
          )
      self.get_stream = channel.unary_stream(
          '/users.Users/get_stream',
          request_serializer=UsersRequest.SerializeToString,
          response_deserializer=UsersReply.FromString,
          )


  class UsersServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_stream(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'get': grpc.unary_unary_rpc_method_handler(
            servicer.get,
            request_deserializer=UsersRequest.FromString,
            response_serializer=UsersReply.SerializeToString,
        ),
        'get_stream': grpc.unary_stream_rpc_method_handler(
            servicer.get_stream,
            request_deserializer=UsersRequest.FromString,
            response_serializer=UsersReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'users.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaUsersServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_stream(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaUsersStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def get(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    get.future = None
    def get_stream(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_Users_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('users.Users', 'get'): UsersRequest.FromString,
      ('users.Users', 'get_stream'): UsersRequest.FromString,
    }
    response_serializers = {
      ('users.Users', 'get'): UsersReply.SerializeToString,
      ('users.Users', 'get_stream'): UsersReply.SerializeToString,
    }
    method_implementations = {
      ('users.Users', 'get'): face_utilities.unary_unary_inline(servicer.get),
      ('users.Users', 'get_stream'): face_utilities.unary_stream_inline(servicer.get_stream),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Users_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('users.Users', 'get'): UsersRequest.SerializeToString,
      ('users.Users', 'get_stream'): UsersRequest.SerializeToString,
    }
    response_deserializers = {
      ('users.Users', 'get'): UsersReply.FromString,
      ('users.Users', 'get_stream'): UsersReply.FromString,
    }
    cardinalities = {
      'get': cardinality.Cardinality.UNARY_UNARY,
      'get_stream': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'users.Users', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
