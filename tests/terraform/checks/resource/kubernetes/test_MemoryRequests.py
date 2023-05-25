import unittest
from pathlib import Path

from checkov.runner_filter import RunnerFilter
from checkov.terraform.checks.resource.kubernetes.MemoryRequests import check
from checkov.terraform.runner import Runner


class TestMemoryRequests(unittest.TestCase):
    def test(self):
        # given
        test_files_dir = Path(__file__).parent / "example_MemoryRequests"

        # when
        report = Runner().run(root_folder=str(test_files_dir), runner_filter=RunnerFilter(checks=[check.id]))

        # then
        summary = report.get_summary()

        passing_resources = {
            "kubernetes_pod.pass",
            "kubernetes_pod_v1.pass",
            "kubernetes_deployment.pass",
            "kubernetes_deployment_v1.pass",
        }

        failing_resources = {
            "kubernetes_pod.fail",
            "kubernetes_pod.fail2",
            "kubernetes_pod.fail3",
            "kubernetes_pod.fail4",
            "kubernetes_pod_v1.fail",
            "kubernetes_pod_v1.fail2",
            "kubernetes_pod_v1.fail3",
            "kubernetes_pod_v1.fail4",
            "kubernetes_deployment.fail",
            "kubernetes_deployment.fail2",
            "kubernetes_deployment.fail3",
            "kubernetes_deployment.fail4",
            "kubernetes_deployment_v1.fail",
            "kubernetes_deployment_v1.fail2",
            "kubernetes_deployment_v1.fail3",
            "kubernetes_deployment_v1.fail4",
        }

        passed_check_resources = {c.resource for c in report.passed_checks}
        failed_check_resources = {c.resource for c in report.failed_checks}

        self.assertEqual(summary["passed"], 4 * 2)
        self.assertEqual(summary["failed"], 16 * 2)
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)


if __name__ == '__main__':
    unittest.main()