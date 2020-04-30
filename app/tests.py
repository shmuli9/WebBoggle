import time

from app.models import Board
from app.solver import generate_valid_words
from app.wordtree import wt


def run_generator(board):
    start = time.time()
    word_list = generate_valid_words(board)
    end = time.time()

    print(f"{len(word_list)} words were generated in {(end - start) * 1000:.6f}ms")
    return sorted(word_list)


def verify_algo(strict=False):
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

    if not strict:
        # run_generator(Board("QuEENPOCIHBIEGKLS"))
        print("\nRandom boards:")
        print("-" * 20)
        for _ in range(1):
            run_generator(Board())

    if output == expected_output[test_dice]:
        return True
    return False


def test_suite(num_runs=10, do_duplicate_analysis=False):
    def avg(numbers):
        total = 0
        for el in numbers:
            total += el
        return total / len(numbers)

    dice = ["QuEENPOCIHBIEGKLS", "LOPGPOCIHBIEGKLS", "EDRQuHIECTSAZNLSE"]

    run_times = []
    interesting_dice = []
    for run in range(num_runs):
        wt.resetTree()
        # d = dice[0] if run % 2 == 0 else dice[1]
        d = ""
        start = time.time()
        board = Board(d)
        word_list = generate_valid_words(board, do_duplicate_analysis)
        end = time.time()

        time_taken = end - start

        if time_taken < 0.00000111111111111111:
            interesting_dice.append(board.dice)
        run_times.append(end - start)
        del word_list, start, end, board

    precision = 6
    print(
        f"average run time over {num_runs} random boards was: {avg(run_times) * 1000:.{precision}f}ms (total:{sum(run_times):.{precision}f}s)")
    print(f"max run time was {max(run_times) * 1000:.{precision}f}ms")
    print(f"min run time was {min(run_times) * 1000}ms")
    print(f"delta (max - min) run time was {(max(run_times) - min(run_times)) * 1000:.{precision}f}ms")
    print(f"Interesting (sub 1/1000 of a ms): {interesting_dice}")
    # print(run_times[:1000])


if not verify_algo(True):
    print("❌ - Algo failed to run successfully on Preconfigured board ")
else:
    print("Algo verified, running test suite")
    # test_suite(10, True)
    test_suite(100)


# def checkWordTree(wordList, wordTree):
#     print("checking wordtree")
#     missed_words = []
#     for word in wordList:
#         if not wordTree.findString(word):
#             missed_words.append(word)
#     print("finished checking wordtree")
#     print(len(missed_words), " words were skipped:\n", missed_words)

# checkWordTree(words, wt)
