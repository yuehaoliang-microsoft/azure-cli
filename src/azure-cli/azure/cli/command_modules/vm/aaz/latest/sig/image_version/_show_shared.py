# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sig image-version show-shared",
)
class ShowShared(AAZCommand):
    """Get an image version in a gallery shared directly to your subscription or tenant

    :example: Get an image version in a gallery shared directly to your subscription or tenant in the given location.
        az sig image-version show-shared --gallery-unique-name galleryUniqueName --gallery-image-definition MyImage --gallery-image-version 1.0.0 --location myLocation
    """

    _aaz_info = {
        "version": "2022-01-03",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.compute/locations/{}/sharedgalleries/{}/images/{}/versions/{}", "2022-01-03"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.gallery_image_definition = AAZStrArg(
            options=["-i", "--gallery-image-name", "--gallery-image-definition"],
            help="The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.gallery_image_version_name = AAZStrArg(
            options=["-e", "--gallery-image-version", "--gallery-image-version-name"],
            help="The name of the gallery image version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>",
            required=True,
            id_part="child_name_3",
        )
        _args_schema.gallery_unique_name = AAZStrArg(
            options=["--gallery-unique-name"],
            help="The unique name of the Shared Gallery.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.location = AAZResourceLocationArg(
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SharedGalleryImageVersionsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SharedGalleryImageVersionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/sharedGalleries/{galleryUniqueName}/images/{galleryImageName}/versions/{galleryImageVersionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "galleryImageName", self.ctx.args.gallery_image_definition,
                    required=True,
                ),
                **self.serialize_url_param(
                    "galleryImageVersionName", self.ctx.args.gallery_image_version_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "galleryUniqueName", self.ctx.args.gallery_unique_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "location", self.ctx.args.location,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-03",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.identifier = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            identifier = cls._schema_on_200.identifier
            identifier.unique_id = AAZStrType(
                serialized_name="uniqueId",
            )

            properties = cls._schema_on_200.properties
            properties.end_of_life_date = AAZStrType(
                serialized_name="endOfLifeDate",
            )
            properties.exclude_from_latest = AAZBoolType(
                serialized_name="excludeFromLatest",
            )
            properties.published_date = AAZStrType(
                serialized_name="publishedDate",
            )
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )

            storage_profile = cls._schema_on_200.properties.storage_profile
            storage_profile.data_disk_images = AAZListType(
                serialized_name="dataDiskImages",
            )
            storage_profile.os_disk_image = AAZObjectType(
                serialized_name="osDiskImage",
            )

            data_disk_images = cls._schema_on_200.properties.storage_profile.data_disk_images
            data_disk_images.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.storage_profile.data_disk_images.Element
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
                flags={"read_only": True},
            )
            _element.host_caching = AAZStrType(
                serialized_name="hostCaching",
            )
            _element.lun = AAZIntType(
                flags={"required": True},
            )

            os_disk_image = cls._schema_on_200.properties.storage_profile.os_disk_image
            os_disk_image.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
                flags={"read_only": True},
            )
            os_disk_image.host_caching = AAZStrType(
                serialized_name="hostCaching",
            )

            return cls._schema_on_200


class _ShowSharedHelper:
    """Helper class for ShowShared"""


__all__ = ["ShowShared"]