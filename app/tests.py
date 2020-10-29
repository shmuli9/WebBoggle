import time

from app.models import Board
from app.solver import generate_valid_words
from app.wordtree import wt
from app.config import Config


def run_generator(board):
    start = time.time()
    word_list = generate_valid_words(board)
    end = time.time()

    print(f"\t{len(word_list)} words were generated in {(end - start) * 1000:.{Config.PRECISION}f}ms")
    return sorted(word_list)


def verify_algo():
    """
    Regression test to ensure that the algorithm is working
    :param strict:
    :return:
    """
    print("\nAttempting to verify algo...")
    if not strict:
        print("\nPreconfigured board:")
        print("-" * 20)
    test_dice = "LOPGPOCIHBIEGKLS"
    # "EDRQuHIECTSAZNLSE"
    output = run_generator(Board(test_dice))
    # print(output)

    expected_output = {
        "EDRQuHIECTSAZNLSE": ['ACE', 'ACED', 'ACER', 'ACES', 'ACQuEST', 'ACRE', 'ACRED', 'ACRES', 'ACRID', 'ACRIDEST',
                              'AERIE', 'AERIED',
                              'AESIR', 'AID', 'AIDE', 'AIDER', 'AIDES', 'AIR', 'AIRED', 'AIREST', 'AIS', 'AIT', 'AITS',
                              'ALS', 'ALT', 'ALTS',
                              'ASH', 'ASHED', 'ASHIER', 'ASIDE', 'ASS', 'ASSEZ', 'ASTIR', 'CAID', 'CAIRD', 'CAL',
                              'CALS', 'CASE', 'CASED',
                              'CASH', 'CASHED', 'CASHIER', 'CASSIE', 'CAST', 'CAZ', 'CEAS', 'CEASE', 'CEAZE', 'CEAZES',
                              'CEDE', 'CEDI',
                              'CEDIS',
                              'CERIA', 'CERIAS', 'CESS', 'CESSE', 'CESTI', 'CREASE', 'CRED', 'CREDIT', 'CREDITS',
                              'CRESS', 'CREST', 'CRIA',
                              'CRIAS', 'CRIED', 'CRIES', 'CRIS', 'CRISE', 'CRISSA', 'CRISSAL', 'CRIT', 'CRITH',
                              'CRITHS', 'CRITS', 'DEAIR',
                              'DEAL', 'DEALS', 'DEALT', 'DEASH', 'DECAL', 'DECALS', 'DECRIAL', 'DECRIALS', 'DEI',
                              'DEISEAL', 'DEISEALS',
                              'DEIST',
                              'DESALT', 'DESHI', 'DESI', 'DESSE', 'DIAL', 'DIALS', 'DIE', 'DIES', 'DIRE', 'DIREST',
                              'DIS', 'DISA', 'DISAS',
                              'DISEASE', 'DISH', 'DISS', 'DIT', 'DITS', 'DRESS', 'DREST', 'DRIES', 'DRIEST', 'EAS',
                              'EASE', 'EASED', 'EASER',
                              'EASIED', 'EASIER', 'EAST', 'EDH', 'EDHS', 'EDIT', 'EDITS', 'EHS', 'EIDE', 'EIDER',
                              'EISH', 'ESS', 'ESSE',
                              'EST',
                              'HEDER', 'HEID', 'HEIR', 'HEIRED', 'HEIRESS', 'HEIST', 'HID', 'HIDE', 'HIDER', 'HIDES',
                              'HIE', 'HIED', 'HIES',
                              'HIRE', 'HIRED', 'HIRES', 'HIS', 'HISN', 'HISS', 'HIST', 'HIT', 'HITS', 'IDE', 'IDEA',
                              'IDEAL', 'IDEALS',
                              'IDEAS',
                              'IDES', 'IRE', 'IRED', 'IRES', 'ISH', 'ITS', 'LAC', 'LACE', 'LACED', 'LACER', 'LACES',
                              'LACQuER', 'LAER',
                              'LAESIE',
                              'LAID', 'LAIR', 'LAIRD', 'LAIRED', 'LAISSE', 'LAITH', 'LAS', 'LASE', 'LASED', 'LASER',
                              'LASH', 'LASHED',
                              'LASS',
                              'LASSI', 'LASSIE', 'LAST', 'LAZE', 'LAZED', 'LAZES', 'NTH', 'QuERIED', 'QuERIST', 'QuEST',
                              'QuEZAL', 'QuEZALS',
                              'REAIS', 'REAL', 'REALS', 'REALTIE', 'REAST', 'REC', 'RECAL', 'RECALS', 'RECAST', 'RED',
                              'REDE', 'REDIA',
                              'REDIAE',
                              'REDIAL', 'REDIALS', 'REDIAS', 'REI', 'REIS', 'REIST', 'RES', 'RESAID', 'RESH', 'RESID',
                              'RESIDE', 'RESIT',
                              'REST',
                              'REZ', 'REZES', 'RIA', 'RIAL', 'RIALS', 'RIAS', 'RID', 'RIDE', 'RIDES', 'RISE', 'RIT',
                              'RITS', 'SAC', 'SACQuE',
                              'SACQuES', 'SACRED', 'SACRIST', 'SAE', 'SAI', 'SAID', 'SAIDEST', 'SAIR', 'SAIRED',
                              'SAIREST', 'SAIS', 'SAIST',
                              'SAITH', 'SAITHE', 'SAITHS', 'SAL', 'SALS', 'SALSE', 'SALT', 'SALTIE', 'SALTIER',
                              'SALTIES', 'SALTIRE',
                              'SALTIRES',
                              'SALTISH', 'SALTS', 'SASER', 'SASH', 'SASHED', 'SAZ', 'SAZES', 'SEA', 'SEAL', 'SEALS',
                              'SEAS', 'SEASE',
                              'SEASED',
                              'SEASIDE', 'SEAZE', 'SEAZED', 'SEAZES', 'SEC', 'SED', 'SEI', 'SEIR', 'SER', 'SERIAL',
                              'SERIALS', 'SEZ', 'SHE',
                              'SHED', 'SHIED', 'SHIER', 'SHIR', 'SHIRE', 'SHIRED', 'SHIT', 'SIAL', 'SIALS', 'SIDE',
                              'SIDER', 'SIDH', 'SIDHE',
                              'SIR', 'SIRE', 'SIRED', 'SIT', 'SITH', 'SITHE', 'SITHED', 'SLAE', 'SLAES', 'SLAID',
                              'SLASH', 'SLASHED', 'STIE',
                              'STIED', 'STIR', 'STIRE', 'STIRED', 'THE', 'THEIR', 'THIR', 'THIRD', 'THIS', 'TID',
                              'TIDE', 'TIDES', 'TIE',
                              'TIED',
                              'TIER', 'TIES', 'TIRE', 'TIRED', 'TIRES', 'TIS', 'ZAIDEH', 'ZAIDEHS', 'ZAIRE', 'ZAIRES',
                              'ZAS', 'ZEA', 'ZEAL',
                              'ZEALS', 'ZEAS', 'ZED', 'ZEST'],
        "LOPGPOCIHBIEGKLS": ['BICE', 'BICES', 'BILE', 'BILES', 'BILK', 'BIO', 'BIOPIC', 'BIS', 'BISE', 'BOH', 'BOI',
                             'BOIL', 'BOILS',
                             'BOIS', 'BOLO', 'BOO', 'BOOL', 'BOP', 'CEIL', 'CEILS', 'CEL', 'CELS', 'CIBOL', 'CIEL',
                             'CIELS', 'CIG',
                             'CIS', 'COB', 'COBLE', 'COBLES', 'COIL', 'COILS', 'COL', 'COLOBI', 'COO', 'COOL', 'COOP',
                             'COP',
                             'COPIES', 'ECO', 'EIK', 'ELK', 'ELS', 'GIE', 'GIES', 'GIP', 'HOB', 'HOC', 'HOI', 'HOIK',
                             'HOIS',
                             'HOISE', 'HOLO', 'HOLP', 'HOO', 'HOOP', 'HOP', 'ICE', 'ICES', 'ILK', 'ISLE', 'KIS', 'LEI',
                             'LEIS',
                             'LES', 'LIB', 'LICE', 'LIE', 'LIES', 'LIS', 'LOB', 'LOBI', 'LOCI', 'LOCIE', 'LOCIES',
                             'LOCIS', 'LOCO',
                             'LOO', 'LOOBIES', 'LOOIE', 'LOOIES', 'LOOP', 'LOP', 'OBI', 'OBIS', 'OIK', 'OIL', 'OILS',
                             'OIS', 'OOH',
                             'OOP', 'PHO', 'PHOBIC', 'PIC', 'PICE', 'PIE', 'PIES', 'PIG', 'PLOP', 'POCO', 'POH', 'POI',
                             'POIS',
                             'POISE', 'POL', 'POLO', 'POO', 'POOH', 'POOL', 'POOP', 'POP', 'SEC', 'SECO', 'SEI', 'SEIK',
                             'SEIL',
                             'SEL', 'SIB', 'SIC', 'SICE', 'SIK', 'SILE', 'SILK', 'SLICE']}

    return output == expected_output[test_dice]


def test_suite(num_runs=10, do_duplicate_analysis=False):
    """
    Test suite to drill down and time individual runs of the algorithm to get a closer look at the core algorithm
    excluding overhead. Also performs some basic analysis of how run times are distributed

    :param num_runs: number of test runs to do
    :param do_duplicate_analysis:
    :return:
    """
    print("\nStarting inidividual test suite...")

    dice = ["QuEENPOCIHBIEGKLS", "LOPGPOCIHBIEGKLS", "EDRQuHIECTSAZNLSE"]

    run_times = []
    interesting_dice = []
    for run in range(num_runs):
        wt.reset_tree()
        # d = dice[0] if run % 2 == 0 else dice[1]  # use this code to test against predefined dice (possibly a better benchmark...)
        d = ""  # empty string will result in a random boards being generated
        start = time.time()
        board = Board(d)
        word_list = generate_valid_words(board, do_duplicate_analysis)
        end = time.time()

        time_taken = end - start

        if time_taken < 0.00000111111111111111:
            """
            the fact that the time is so low is not due to a super efficient algo, rather it is a quirk in the 
            scheduler (and in any scheduler) and is to be expected, but doesnt really matter
            """
            interesting_dice.append((board.dice, time_taken))

        run_times.append(end - start)
        del word_list, start, end, board

    print(
        f"\tAverage run time over {num_runs} random boards was: {(sum(run_times) / len(run_times)) * 1000:.{Config.PRECISION}f}ms (total:{sum(run_times):.{Config.PRECISION}f}s)")
    print(f"\t\tMaximum run time was {max(run_times) * 1000:.{Config.PRECISION}f}ms")
    print(f"\t\tMinimum run time was {min(run_times) * 1000}ms")


def overall_test(number_of_runs):
    """
    Run the algo `number_of_runs` times to see how the application works as a whole
    :return:
    """
    print("\nStarting overall test...")

    start = time.time()

    dice = ["QuEENPOCIHBIEGKLS", "LOPGPOCIHBIEGKLS", "EDRQuHIECTSAZNLSE"]

    for run in range(number_of_runs):
        wt.reset_tree()
        # d = dice[0] if run % 2 == 0 else dice[1]  # use this code to test against predefined dice (possibly a better benchmark...)
        d = ""  # empty string will result in a random boards being generated

        board = Board(d)
        word_list = generate_valid_words(board)
    end = time.time()

    print(f"\tAverage across {number_of_runs} runs: {((end - start) * 1000) / number_of_runs:.{Config.PRECISION}f}ms")


def check_wordtree(wordTree):
    """
    Regression test to test to ensure that WordTree is working correctly
    """

    print("Checking wordtree")
    wordTree.reset_tree()
    missed_words = []

    with open(Config.DICTIONARY_ADDRESS, encoding="utf8") as file:
        for word in file.read().split("\n"):
            if not wordTree.find(word):
                missed_words.append(word)

    print("Finished checking wordtree")
    return not (len(missed_words) > 0 and not print(len(missed_words), " words were skipped:\n", missed_words[:100]))


if not check_wordtree(wt):
    print("❌ - WordTree verification failed")
elif not verify_algo():
    print("❌ - Algo verification failed to run successfully on Preconfigured board")
else:
    runs = 10000
    print(f"Algo verified, running test suite(s) with {runs} runs:")

    test_suite(runs)
    overall_test(runs)

    print("\nFinished test suite(s)")
