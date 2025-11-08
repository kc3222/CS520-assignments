"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_num_position_1():
    """Test num_position case 1."""
    assert solution.num_position("there are 70 flats in this apartment")==10

def test_num_position_2():
    """Test num_position case 2."""
    assert solution.num_position("every adult have 32 teeth")==17

def test_num_position_3():
    """Test num_position case 3."""
    assert solution.num_position("isha has 79 chocolates in her bag")==9

def test_num_position_4():
    """Test num_position case 4."""
    assert solution.num_position("i463kar0q9w3rtkk7r5im0slj736p7edphcda") == 1

def test_num_position_5():
    """Test num_position case 5."""
    assert solution.num_position("y 1lmacgqjxf9qlbfnghs9uz21jbq9354fa3") == 2

def test_num_position_6():
    """Test num_position case 6."""
    assert solution.num_position("1a7kmayi570gnw90o9 f0ndpv7s8a57040rf0") == 0

def test_num_position_7():
    """Test num_position case 7."""
    assert solution.num_position("4ypd5yf88vmyp9t2jrx3t0x1okczanodkm") == 0

def test_num_position_8():
    """Test num_position case 8."""
    assert solution.num_position("6y2o8984m 5p200o4f1tlf6v7ghk8ty3onkjna") == 0

def test_num_position_9():
    """Test num_position case 9."""
    assert solution.num_position("sf0w0qlfjcmuxcdir r062hvshxk ind0qixeg vv0") == 2

def test_num_position_10():
    """Test num_position case 10."""
    assert solution.num_position("arsducimygtb59j2vx980 1lbiuu4fxp7yk") == 12

def test_num_position_11():
    """Test num_position case 11."""
    assert solution.num_position("79tsaam4zduame8aditvcppwa6wdgw9bnw86") == 0

def test_num_position_12():
    """Test num_position case 12."""
    assert solution.num_position("sw2dga4whwso4ue43kt81hn7bjym93q97a3l5ol2o") == 2

def test_num_position_13():
    """Test num_position case 13."""
    assert solution.num_position("qh82iv4rlutax86t m2mcebw2mngiwtfkh") == 2

def test_num_position_14():
    """Test num_position case 14."""
    assert solution.num_position("7tmz gu1ci26rwmtw8waji713so5w81vz3nlb") == 0

def test_num_position_15():
    """Test num_position case 15."""
    assert solution.num_position("xc0oisb12qzqgbqmv3ly 4sh4y9wdp73835hm3yu2") == 2

def test_num_position_16():
    """Test num_position case 16."""
    assert solution.num_position("328q m7dwfh p421fnkg4hzzbp39h09jv3 xmy9") == 0

def test_num_position_17():
    """Test num_position case 17."""
    assert solution.num_position("8v0 uar55xuatn6glrohfz6bhxawwmc57f") == 0

def test_num_position_18():
    """Test num_position case 18."""
    assert solution.num_position("00hj6ewzygh8rlx8e8uelbyswdppvi3v ask2n7v") == 0

def test_num_position_19():
    """Test num_position case 19."""
    assert solution.num_position("swxrhxrrjumdtivev62oosqx0n9lqmw41wq7w4dr") == 17

def test_num_position_20():
    """Test num_position case 20."""
    assert solution.num_position("vjp7iw1eadygzueb1o0in541ebq8nkj65") == 3

def test_num_position_21():
    """Test num_position case 21."""
    assert solution.num_position("f7af6r4f2k3v8zld61u zuuzvqwbpn45aj1") == 1

def test_num_position_22():
    """Test num_position case 22."""
    assert solution.num_position("q3q3km6w1hiixq74auv5uoudo2tij8ve83ifc5olpa") == 1

def test_num_position_23():
    """Test num_position case 23."""
    assert solution.num_position("nl789fb u6cnqnbripjleny9e 9z0hv7re") == 2

def test_num_position_24():
    """Test num_position case 24."""
    assert solution.num_position("ukomw4vlhzo8v7ofntn8 7vfmy8slymkbrkc6 2") == 5

def test_num_position_25():
    """Test num_position case 25."""
    assert solution.num_position("stx1ko04h78ttjx9xdvnhqbpg7hagxtwyxkz ") == 3

def test_num_position_26():
    """Test num_position case 26."""
    assert solution.num_position("ha4tvdn8q2axxgdqmp8d ekm w0qspegt") == 2

def test_num_position_27():
    """Test num_position case 27."""
    assert solution.num_position("3jzqfj hrgzpe1g3kuxhp1 gxh7gpaqx837d1fe6u") == 0

def test_num_position_28():
    """Test num_position case 28."""
    assert solution.num_position("auclhxat 6wr6w8qh0 b1c5wl2to4nnbsqzihvo") == 9

def test_num_position_29():
    """Test num_position case 29."""
    assert solution.num_position("9rvbuorh52s 1p74843p24c378 a6yeccz") == 0

def test_num_position_30():
    """Test num_position case 30."""
    assert solution.num_position("kz028ewsv0 95tz puylifv9isvs23v8vm") == 2

def test_num_position_31():
    """Test num_position case 31."""
    assert solution.num_position("25xuxsk 8jttqddjdbq7v5 115pr 1zw w") == 0

def test_num_position_32():
    """Test num_position case 32."""
    assert solution.num_position("01ow8lrgovjumr60w7djm zpp 5jzy4m94") == 0

def test_num_position_33():
    """Test num_position case 33."""
    assert solution.num_position("tokukrqc19plec97cjx7ij2l1v7lwz8f5m240") == 8

def test_num_position_34():
    """Test num_position case 34."""
    assert solution.num_position("ced2kr5hgg3ei96pi5yb0 1lovex9o 1joa0n9pkvt") == 3

def test_num_position_35():
    """Test num_position case 35."""
    assert solution.num_position("ym4mxqugv zxwrz9 8sshwk236foyq9im3z") == 2

def test_num_position_36():
    """Test num_position case 36."""
    assert solution.num_position("9p ye31v4spujkwcsw2wvhx7r8fajl6tf2rju3qv4") == 0

def test_num_position_37():
    """Test num_position case 37."""
    assert solution.num_position("j4ahgaabvl72ekwx43j2rumrkx b") == 1

def test_num_position_38():
    """Test num_position case 38."""
    assert solution.num_position("3j14ns9g164wu7fhmiqzpk6e7t") == 0

def test_num_position_39():
    """Test num_position case 39."""
    assert solution.num_position("tm9jsv0l359xyz8qe008zxtbtpw0n7") == 2

def test_num_position_40():
    """Test num_position case 40."""
    assert solution.num_position("bdmhx3odmsw9r1 5pcqn4k9ki") == 5

def test_num_position_41():
    """Test num_position case 41."""
    assert solution.num_position("jr7qyvw11i4yk1dszy72t6") == 2

def test_num_position_42():
    """Test num_position case 42."""
    assert solution.num_position("wcti53w5mewjj416q3t3wn7cn") == 4

def test_num_position_43():
    """Test num_position case 43."""
    assert solution.num_position("uwijsbxks3lf9bkmxky70j0dndem") == 9

def test_num_position_44():
    """Test num_position case 44."""
    assert solution.num_position("trpphqzdfrilcvywhijwk1w ") == 21

def test_num_position_45():
    """Test num_position case 45."""
    assert solution.num_position("xst5k90y11dspblzbfvqkweg9o7c") == 3

def test_num_position_46():
    """Test num_position case 46."""
    assert solution.num_position("t1gmkcasa1wtu2 foo0bj") == 1

def test_num_position_47():
    """Test num_position case 47."""
    assert solution.num_position("7z73i0wenu5suelu51fbi") == 0

def test_num_position_48():
    """Test num_position case 48."""
    assert solution.num_position("k7f8ipejcexdr20if thn4brv") == 1

def test_num_position_49():
    """Test num_position case 49."""
    assert solution.num_position("8xs0hjf4tm4pmmcyy4zd5sgij5h78") == 0

def test_num_position_50():
    """Test num_position case 50."""
    assert solution.num_position("jmzbw7ym1ei89 m11xlfx3qo1bde") == 5

def test_num_position_51():
    """Test num_position case 51."""
    assert solution.num_position("ezl6isa528v2gr1uw0xf8 3cmv e") == 3

def test_num_position_52():
    """Test num_position case 52."""
    assert solution.num_position("3ebjny0x1cnbo7ghmi211zz9c 7") == 0

def test_num_position_53():
    """Test num_position case 53."""
    assert solution.num_position("69n46pti7ny0al0wgvvwd") == 0

def test_num_position_54():
    """Test num_position case 54."""
    assert solution.num_position("o xlaidu22k10mgtzxpw26gel") == 8

def test_num_position_55():
    """Test num_position case 55."""
    assert solution.num_position("9c8nqhsod ggc03u7bu20e1") == 0

def test_num_position_56():
    """Test num_position case 56."""
    assert solution.num_position("asf7dsn17pvfotsbqwyahstllqpp2") == 3

def test_num_position_57():
    """Test num_position case 57."""
    assert solution.num_position("f7evdwvt8bj45dxwxc7cr8z374") == 1

def test_num_position_58():
    """Test num_position case 58."""
    assert solution.num_position("cffbeemi6alfxb8oztc67sp4tf") == 8

def test_num_position_59():
    """Test num_position case 59."""
    assert solution.num_position("e039y1wl9ccb5bwcinnoo726lm98c") == 1

def test_num_position_60():
    """Test num_position case 60."""
    assert solution.num_position("wsdsf 6yvxe71rcohnyt3 ") == 6

def test_num_position_61():
    """Test num_position case 61."""
    assert solution.num_position("i5b7nqu rc7trqx7txgqvftpr") == 1

def test_num_position_62():
    """Test num_position case 62."""
    assert solution.num_position("h08mbglfjhu2zi8039tzu") == 1

def test_num_position_63():
    """Test num_position case 63."""
    assert solution.num_position("hf wk5x5a7cuaztaw1zl44y82low9w") == 5

def test_num_position_64():
    """Test num_position case 64."""
    assert solution.num_position("vn5mec63kc1jw364ak0n4prxxx ") == 2

def test_num_position_65():
    """Test num_position case 65."""
    assert solution.num_position("fh3rqqv1lpl2u5uyw2oox090x") == 2

def test_num_position_66():
    """Test num_position case 66."""
    assert solution.num_position("5yd4amb9dqryy4l0mh84k") == 0

def test_num_position_67():
    """Test num_position case 67."""
    assert solution.num_position("wdj70wxx0y2rr4buscjxtvlr01x") == 3

def test_num_position_68():
    """Test num_position case 68."""
    assert solution.num_position("lry414pq 6987ebm7h7l fqngt ") == 3

def test_num_position_69():
    """Test num_position case 69."""
    assert solution.num_position("b40i8virc8ny2qm v le27 2") == 1

def test_num_position_70():
    """Test num_position case 70."""
    assert solution.num_position("ws9bhg0v1hzs611nw0gspgge8rnl76ga5") == 2

def test_num_position_71():
    """Test num_position case 71."""
    assert solution.num_position("5lu  ujzwti6hgxzvtxqgjkz9gdgumdv 0a") == 0

def test_num_position_72():
    """Test num_position case 72."""
    assert solution.num_position("ttqywwfnm3p6hlbq4k5o8m20asoe94jf") == 9

def test_num_position_73():
    """Test num_position case 73."""
    assert solution.num_position("84flkq2x5nv4uyswy1sngkp4z1xfqnsowsoogyy") == 0

def test_num_position_74():
    """Test num_position case 74."""
    assert solution.num_position("tqwf6wjchq1h0zgc64ltycaj5dlqhrfsvrgf0") == 4

def test_num_position_75():
    """Test num_position case 75."""
    assert solution.num_position("y jzkzp5 6d1mj7h49uq9h4kgtt7ni0a99moc") == 7

def test_num_position_76():
    """Test num_position case 76."""
    assert solution.num_position("u5o nzigve83cl8e3axis0vmu 95d7r3l2nt7") == 1

def test_num_position_77():
    """Test num_position case 77."""
    assert solution.num_position("dr1 cuj5t2b2iytsy6 mz30hqgecqu 9") == 2

def test_num_position_78():
    """Test num_position case 78."""
    assert solution.num_position("0jfgdvqe1ntsk8lfg83srn57vmim7m21vak5") == 0

def test_num_position_79():
    """Test num_position case 79."""
    assert solution.num_position("64obbvk5njaf33artntvfrxyn 2uek4phzbv") == 0

def test_num_position_80():
    """Test num_position case 80."""
    assert solution.num_position("wn84 y1imw vdwtxx2cd8gk8e1yb0n7ejqx") == 2

def test_num_position_81():
    """Test num_position case 81."""
    assert solution.num_position("ha8ityjgkaw jyocvv56qe15yjdc9av6fot9db8") == 2

def test_num_position_82():
    """Test num_position case 82."""
    assert solution.num_position("wmvdw5v7h8ns fzcl1umy7yhplu7y3gaj09e") == 5

def test_num_position_83():
    """Test num_position case 83."""
    assert solution.num_position("833621sfvb7 o672z2qzatnaeknwbyl1yy44 k") == 0

def test_num_position_84():
    """Test num_position case 84."""
    assert solution.num_position("5wvmzd togk y24saio0ddwa edfyqyillx") == 0

def test_num_position_85():
    """Test num_position case 85."""
    assert solution.num_position("4hf1oly40nkkac ce3q 8tmlokkvwa") == 0

def test_num_position_86():
    """Test num_position case 86."""
    assert solution.num_position("z27t5tgzyn6ar7oytrvmtf655o98tqr02i4") == 1

def test_num_position_87():
    """Test num_position case 87."""
    assert solution.num_position("h1 cmcfbc2k80upvbvmoi81qap ulauah6fpy2 ") == 1

def test_num_position_88():
    """Test num_position case 88."""
    assert solution.num_position("9u dm7ffnnpvdapc8nqphofim0ivrjxk") == 0

def test_num_position_89():
    """Test num_position case 89."""
    assert solution.num_position("3wbdppff1brvgrmievk2takm6 zf m") == 0

def test_num_position_90():
    """Test num_position case 90."""
    assert solution.num_position("7pjib1dqhhqrqzob6rwnkr1gust3bezat") == 0

def test_num_position_91():
    """Test num_position case 91."""
    assert solution.num_position("bjwem1j08 v7gbc aotvcruzsvejx99vpjkx2l") == 5

def test_num_position_92():
    """Test num_position case 92."""
    assert solution.num_position("jz9fsp0yluv2p1mmylwbuincnlfqhjrqc7") == 2

def test_num_position_93():
    """Test num_position case 93."""
    assert solution.num_position("3gyr4yaq6uolklsc93d6js58cjaa8f") == 0

def test_num_position_94():
    """Test num_position case 94."""
    assert solution.num_position("0w8i0dkblx9g03p123awj0mqb39a5efe1p") == 0

def test_num_position_95():
    """Test num_position case 95."""
    assert solution.num_position("weylzblvcyi5vjeia316r0v922z6ic") == 11

def test_num_position_96():
    """Test num_position case 96."""
    assert solution.num_position("3gtmcaygyb2ncfxytiaysjv72jx27u0rl") == 0

def test_num_position_97():
    """Test num_position case 97."""
    assert solution.num_position("pn efsxk39dzer6nj92oafv3iju3ue") == 8

def test_num_position_98():
    """Test num_position case 98."""
    assert solution.num_position("mafy7992f 3hkxbg6i3q904eowft2ow ") == 4

def test_num_position_99():
    """Test num_position case 99."""
    assert solution.num_position("9o5ucvqjvs2qu8404yqrgzcreqhkxvop") == 0

def test_num_position_100():
    """Test num_position case 100."""
    assert solution.num_position("qwd8delx8hfbaechjszoio7ndbkgyhddfdu9dw5") == 3

def test_num_position_101():
    """Test num_position case 101."""
    assert solution.num_position("w3m58kdjiv7sce2vrh76 5hm42husf7x17j30rl") == 1

def test_num_position_102():
    """Test num_position case 102."""
    assert solution.num_position(" jjnbz cu feimytxhmt0syab0rye5m") == 20
