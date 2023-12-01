# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import name_resolution_pb2 as name__resolution__pb2


class NameResolutionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/NameResolution/Register',
                request_serializer=name__resolution__pb2.ServiceInfo.SerializeToString,
                response_deserializer=name__resolution__pb2.Result.FromString,
                )
        self.Lookup = channel.unary_unary(
                '/NameResolution/Lookup',
                request_serializer=name__resolution__pb2.ServiceName.SerializeToString,
                response_deserializer=name__resolution__pb2.Endpoint.FromString,
                )
        self.Unregister = channel.unary_unary(
                '/NameResolution/Unregister',
                request_serializer=name__resolution__pb2.ServiceName.SerializeToString,
                response_deserializer=name__resolution__pb2.Result.FromString,
                )
        self.AllServices = channel.unary_unary(
                '/NameResolution/AllServices',
                request_serializer=name__resolution__pb2.Empty.SerializeToString,
                response_deserializer=name__resolution__pb2.Services.FromString,
                )


class NameResolutionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lookup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unregister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllServices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameResolutionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=name__resolution__pb2.ServiceInfo.FromString,
                    response_serializer=name__resolution__pb2.Result.SerializeToString,
            ),
            'Lookup': grpc.unary_unary_rpc_method_handler(
                    servicer.Lookup,
                    request_deserializer=name__resolution__pb2.ServiceName.FromString,
                    response_serializer=name__resolution__pb2.Endpoint.SerializeToString,
            ),
            'Unregister': grpc.unary_unary_rpc_method_handler(
                    servicer.Unregister,
                    request_deserializer=name__resolution__pb2.ServiceName.FromString,
                    response_serializer=name__resolution__pb2.Result.SerializeToString,
            ),
            'AllServices': grpc.unary_unary_rpc_method_handler(
                    servicer.AllServices,
                    request_deserializer=name__resolution__pb2.Empty.FromString,
                    response_serializer=name__resolution__pb2.Services.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameResolution', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameResolution(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameResolution/Register',
            name__resolution__pb2.ServiceInfo.SerializeToString,
            name__resolution__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Lookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameResolution/Lookup',
            name__resolution__pb2.ServiceName.SerializeToString,
            name__resolution__pb2.Endpoint.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unregister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameResolution/Unregister',
            name__resolution__pb2.ServiceName.SerializeToString,
            name__resolution__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameResolution/AllServices',
            name__resolution__pb2.Empty.SerializeToString,
            name__resolution__pb2.Services.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
