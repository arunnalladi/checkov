from typing import Any

from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories
from checkov.common.models.consts import ANY_VALUE


class NeptuneClusterEncryptedWithCMK(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure Neptune is encrypted by KMS using a customer managed Key (CMK)"
        id = "CKV_AWS_347"
        supported_resources = ("aws_neptune_cluster",)
        categories = (CheckCategories.ENCRYPTION,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "kms_key_arn"

    def get_expected_value(self) -> Any:
        return ANY_VALUE


check = NeptuneClusterEncryptedWithCMK()
