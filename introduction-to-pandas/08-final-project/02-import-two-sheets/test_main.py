from solution import *


def test_01_sales_sheet():
    """Read the supplied sales text into the first returned table"""
    for text in [SALES_CSV, "sale_id,units\n41,7\n42,2\n"]:
        actual, _ = read_tables(text, STALLS_CSV)
        pd.testing.assert_frame_equal(actual, pd.read_csv(StringIO(text)))


def test_02_directory_sheet():
    """Read the supplied directory into the second returned table"""
    for text in [STALLS_CSV, "stall_id,stall_name,neighborhood\nQ,Seeds,West\n"]:
        _, actual = read_tables(SALES_CSV, text)
        pd.testing.assert_frame_equal(actual, pd.read_csv(StringIO(text)))
