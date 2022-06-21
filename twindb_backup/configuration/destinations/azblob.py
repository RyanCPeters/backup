"""Azure-blob storage destination configuration"""
import os
from typing import AnyStr, Optional


class AzureBlobConf:
    def __init__(
        self,
        remote_path: str,
        connection_string: str,
        can_do_overwrites: str = "False",
        cpu_cap: str = "",
        max_mem_bytes: str = "",
        default_protocol: Optional[AnyStr] = "",
        default_host_name: Optional[AnyStr] = "",
        default_container_name: Optional[AnyStr] = "",
        default_interval: Optional[AnyStr] = "",
        default_media_type: Optional[AnyStr] = "",
        default_fname_prefix: Optional[AnyStr] = "",
    ):
        """Azure-blob destination configuration.

        Azure Blob Storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that
        doesn't adhere to a particular data model or definition, such as text or binary data. Blob storage offers three
        types of resources.

        See: https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python#object-model

        :param connection_string: A string object;
                                  The connection string as described here:
                                  https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python#copy-your-credentials-from-the-azure-portal

        :param default_container_name: A string-like or list of string-like object.
                               A string-like object is generally a str or bytes object.
        """
        super(AzureBlobConf, self).__init__()
        self._remote_path = remote_path.strip("'")
        self._connection_string = connection_string.strip("'")
        self._can_do_overwrites = can_do_overwrites.strip("'").lower() == "true"
        self._cpu_cap = int(cpu_cap.strip("'")) if cpu_cap else max(os.cpu_count() - 1, 1)
        self._max_mem_bytes = int(max_mem_bytes.strip("'")) if max_mem_bytes else 2**24
        self._default_protocol = default_protocol.strip("'")
        self._default_container_name = default_container_name.strip("'")
        self._default_host_name = default_host_name.strip("'")
        self._default_interval = default_interval.strip("'")
        self._default_media_type = default_media_type.strip("'")
        self._default_fname_prefix = default_fname_prefix.strip("'")

    @property
    def remote_path(self):
        return self._remote_path

    @property
    def connection_string(self):
        return self._connection_string

    @property
    def can_do_overwrites(self):
        return self._can_do_overwrites

    @property
    def cpu_cap(self):
        return self._cpu_cap

    @property
    def max_mem_bytes(self):
        return self._max_mem_bytes

    @property
    def default_protocol(self):
        return self._default_protocol

    @property
    def default_container_name(self):
        return self._default_container_name

    @property
    def default_host_name(self):
        return self._default_host_name

    @property
    def default_interval(self):
        return self._default_interval

    @property
    def default_media_type(self):
        return self._default_media_type

    @property
    def default_fname_prefix(self):
        return self._default_fname_prefix

    @property
    def destination_kwargs(self):
        return {
            attr: getattr(self, attr)
            for attr in (
                "remote_path",
                "connection_string",
                "can_do_overwrites",
                "cpu_cap",
                "max_mem_bytes",
                "default_protocol",
                "default_host_name",
                "default_container_name",
                "default_interval",
                "default_media_type",
                "default_fname_prefix",
            )
        }
