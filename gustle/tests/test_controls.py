import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)

    def test_index(self):
        with open("data/test.cgst.checksum") as f:
            cgst_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(cgst_checksum, "f7c03c7ec44ce1dca23dadc01f7d41a42da90940f34d4241ad86f0cd5f19fc55")
        
    def test_summary(self):
        with open("data/test_summary.tsv.checksum") as f:
            summary_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(summary_checksum, "e6be9f3feff1230f7e4896cb3c8fc21186add20a8868fdf91b2ca04942d801f3")
        
        # # Check gustle index
        # index_command = "gustle index --cgst data/test.cgst --output data/test_query.gus data/test_query.fa.gz"
        # index_process = subprocess.Popen(index_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # index_out, index_err = index_process.communicate()
        # # Processing steps are saved to index_err
        # check_index = re.search(r'.*(INFO: saving.*:.*\n)', index_err.decode('utf-8'))
        # self.assertEqual(check_index.group(1), "INFO: saving index to data/test_query.gus: done\n")

        # # Check gustle genotype
        # genotype_command = "gustle genotype --index data/test_query.gus data/test_cgst.fa"
        # genotype_process = subprocess.Popen(genotype_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # genotype_out, genotype_err = genotype_process.communicate()
        # self.assertEqual(genotype_out, b'Filename\tcgST\tquery1matches\tquery1rev\tquery4\tquery6genome2match\ndata/test_cgst.fa\t1 (4/8)\t0\t0\t1\t16\n')


if __name__ == '__main__':
    unittest.main()