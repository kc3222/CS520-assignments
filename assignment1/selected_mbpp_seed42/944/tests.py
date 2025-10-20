'''chatgpt'''
'''cot'''
# Run 1: Fail
# import re

# def num_position(text):
#     return [(m.group(), m.start()) for m in re.finditer(r'\d+', text)]

# Run 2: Fail
# import re

# def num_position(text):
#     return [(m.group(), m.start()) for m in re.finditer(r'\d+', text)]

# Run 3: Fail
# import re

# def num_position(text):
#     return [(m.group(), m.start()) for m in re.finditer(r'\d+', text)]

'''self-planning'''
# Run 1: Fail
# import re

# def num_position(text):
#     return [(num, i.start()) for i in re.finditer(r'\d+', text) for num in [i.group()]]

# Run 2: Fail
# import re

# def num_position(text):
#     return [(match.group(), match.start()) for match in re.finditer(r'\d+', text)]

# Run 3: Fail
# import re

# def num_position(text):
#     return [(m.group(), m.start()) for m in re.finditer(r'\d+', text)]

'''claude'''
'''cot'''
# Run 1: Fail
# def num_position(text):
#     for i, char in enumerate(text):
#         if char.isdigit():
#             print(f"Position {i}: {char}")

# Run 2: Fail
# def num_position(text):
#     i = 0
#     while i < len(text):
#         if text[i].isdigit():
#             start = i
#             num = ''
#             while i < len(text) and text[i].isdigit():
#                 num += text[i]
#                 i += 1
#             print(f"Number: {num}, Position: {start}")
#         else:
#             i += 1
#     return i

# Run 3: Fail
# def num_position(text):
#     i = 0
#     while i < len(text):
#         if text[i].isdigit():
#             start = i
#             num = ''
#             while i < len(text) and text[i].isdigit():
#                 num += text[i]
#                 i += 1
#             print(f"{num} at position {start}")
#         else:
#             i += 1
#     return i

'''self-planning'''
# Run 1: Fail
def num_position(text):
    i = 0
    while i < len(text):
        if text[i].isdigit():
            start = i
            num = ''
            while i < len(text) and text[i].isdigit():
                num += text[i]
                i += 1
            print(f"{num} {start}")
        else:
            i += 1
    return i

# Run 2: Fail
def num_position(text):
    i = 0
    while i < len(text):
        if text[i].isdigit():
            start = i
            num = ''
            while i < len(text) and text[i].isdigit():
                num += text[i]
                i += 1
            print(f"{num} {start}")
        else:
            i += 1
    return i

# Run 3: Fail
def num_position(text):
    i = 0
    while i < len(text):
        if text[i].isdigit():
            start = i
            num = ''
            while i < len(text) and text[i].isdigit():
                num += text[i]
                i += 1
            print(f"{num} {start}")
        else:
            i += 1
    return i


'''Fixed by adding tests'''
'''chatgpt'''
def num_position(text):
    for i, ch in enumerate(text):
        if ch.isdigit():
            return i
    return -1

'''claude'''
def num_position(text):
    for i, char in enumerate(text):
        if char.isdigit():
            return i
    return -1

assert num_position("there are 70 flats in this apartment")==10
assert num_position("every adult have 32 teeth")==17
assert num_position("isha has 79 chocolates in her bag")==9
assert num_position("i463kar0q9w3rtkk7r5im0slj736p7edphcda") == 1
assert num_position("y 1lmacgqjxf9qlbfnghs9uz21jbq9354fa3") == 2
assert num_position("1a7kmayi570gnw90o9 f0ndpv7s8a57040rf0") == 0
assert num_position("4ypd5yf88vmyp9t2jrx3t0x1okczanodkm") == 0
assert num_position("6y2o8984m 5p200o4f1tlf6v7ghk8ty3onkjna") == 0
assert num_position("sf0w0qlfjcmuxcdir r062hvshxk ind0qixeg vv0") == 2
assert num_position("arsducimygtb59j2vx980 1lbiuu4fxp7yk") == 12
assert num_position("79tsaam4zduame8aditvcppwa6wdgw9bnw86") == 0
assert num_position("sw2dga4whwso4ue43kt81hn7bjym93q97a3l5ol2o") == 2
assert num_position("qh82iv4rlutax86t m2mcebw2mngiwtfkh") == 2
assert num_position("7tmz gu1ci26rwmtw8waji713so5w81vz3nlb") == 0
assert num_position("xc0oisb12qzqgbqmv3ly 4sh4y9wdp73835hm3yu2") == 2
assert num_position("328q m7dwfh p421fnkg4hzzbp39h09jv3 xmy9") == 0
assert num_position("8v0 uar55xuatn6glrohfz6bhxawwmc57f") == 0
assert num_position("00hj6ewzygh8rlx8e8uelbyswdppvi3v ask2n7v") == 0
assert num_position("swxrhxrrjumdtivev62oosqx0n9lqmw41wq7w4dr") == 17
assert num_position("vjp7iw1eadygzueb1o0in541ebq8nkj65") == 3
assert num_position("f7af6r4f2k3v8zld61u zuuzvqwbpn45aj1") == 1
assert num_position("q3q3km6w1hiixq74auv5uoudo2tij8ve83ifc5olpa") == 1
assert num_position("nl789fb u6cnqnbripjleny9e 9z0hv7re") == 2
assert num_position("ukomw4vlhzo8v7ofntn8 7vfmy8slymkbrkc6 2") == 5
assert num_position("stx1ko04h78ttjx9xdvnhqbpg7hagxtwyxkz ") == 3
assert num_position("ha4tvdn8q2axxgdqmp8d ekm w0qspegt") == 2
assert num_position("3jzqfj hrgzpe1g3kuxhp1 gxh7gpaqx837d1fe6u") == 0
assert num_position("auclhxat 6wr6w8qh0 b1c5wl2to4nnbsqzihvo") == 9
assert num_position("9rvbuorh52s 1p74843p24c378 a6yeccz") == 0
assert num_position("kz028ewsv0 95tz puylifv9isvs23v8vm") == 2
assert num_position("25xuxsk 8jttqddjdbq7v5 115pr 1zw w") == 0
assert num_position("01ow8lrgovjumr60w7djm zpp 5jzy4m94") == 0
assert num_position("tokukrqc19plec97cjx7ij2l1v7lwz8f5m240") == 8
assert num_position("ced2kr5hgg3ei96pi5yb0 1lovex9o 1joa0n9pkvt") == 3
assert num_position("ym4mxqugv zxwrz9 8sshwk236foyq9im3z") == 2
assert num_position("9p ye31v4spujkwcsw2wvhx7r8fajl6tf2rju3qv4") == 0
assert num_position("j4ahgaabvl72ekwx43j2rumrkx b") == 1
assert num_position("3j14ns9g164wu7fhmiqzpk6e7t") == 0
assert num_position("tm9jsv0l359xyz8qe008zxtbtpw0n7") == 2
assert num_position("bdmhx3odmsw9r1 5pcqn4k9ki") == 5
assert num_position("jr7qyvw11i4yk1dszy72t6") == 2
assert num_position("wcti53w5mewjj416q3t3wn7cn") == 4
assert num_position("uwijsbxks3lf9bkmxky70j0dndem") == 9
assert num_position("trpphqzdfrilcvywhijwk1w ") == 21
assert num_position("xst5k90y11dspblzbfvqkweg9o7c") == 3
assert num_position("t1gmkcasa1wtu2 foo0bj") == 1
assert num_position("7z73i0wenu5suelu51fbi") == 0
assert num_position("k7f8ipejcexdr20if thn4brv") == 1
assert num_position("8xs0hjf4tm4pmmcyy4zd5sgij5h78") == 0
assert num_position("jmzbw7ym1ei89 m11xlfx3qo1bde") == 5
assert num_position("ezl6isa528v2gr1uw0xf8 3cmv e") == 3
assert num_position("3ebjny0x1cnbo7ghmi211zz9c 7") == 0
assert num_position("69n46pti7ny0al0wgvvwd") == 0
assert num_position("o xlaidu22k10mgtzxpw26gel") == 8
assert num_position("9c8nqhsod ggc03u7bu20e1") == 0
assert num_position("asf7dsn17pvfotsbqwyahstllqpp2") == 3
assert num_position("f7evdwvt8bj45dxwxc7cr8z374") == 1
assert num_position("cffbeemi6alfxb8oztc67sp4tf") == 8
assert num_position("e039y1wl9ccb5bwcinnoo726lm98c") == 1
assert num_position("wsdsf 6yvxe71rcohnyt3 ") == 6
assert num_position("i5b7nqu rc7trqx7txgqvftpr") == 1
assert num_position("h08mbglfjhu2zi8039tzu") == 1
assert num_position("hf wk5x5a7cuaztaw1zl44y82low9w") == 5
assert num_position("vn5mec63kc1jw364ak0n4prxxx ") == 2
assert num_position("fh3rqqv1lpl2u5uyw2oox090x") == 2
assert num_position("5yd4amb9dqryy4l0mh84k") == 0
assert num_position("wdj70wxx0y2rr4buscjxtvlr01x") == 3
assert num_position("lry414pq 6987ebm7h7l fqngt ") == 3
assert num_position("b40i8virc8ny2qm v le27 2") == 1
assert num_position("ws9bhg0v1hzs611nw0gspgge8rnl76ga5") == 2
assert num_position("5lu  ujzwti6hgxzvtxqgjkz9gdgumdv 0a") == 0
assert num_position("ttqywwfnm3p6hlbq4k5o8m20asoe94jf") == 9
assert num_position("84flkq2x5nv4uyswy1sngkp4z1xfqnsowsoogyy") == 0
assert num_position("tqwf6wjchq1h0zgc64ltycaj5dlqhrfsvrgf0") == 4
assert num_position("y jzkzp5 6d1mj7h49uq9h4kgtt7ni0a99moc") == 7
assert num_position("u5o nzigve83cl8e3axis0vmu 95d7r3l2nt7") == 1
assert num_position("dr1 cuj5t2b2iytsy6 mz30hqgecqu 9") == 2
assert num_position("0jfgdvqe1ntsk8lfg83srn57vmim7m21vak5") == 0
assert num_position("64obbvk5njaf33artntvfrxyn 2uek4phzbv") == 0
assert num_position("wn84 y1imw vdwtxx2cd8gk8e1yb0n7ejqx") == 2
assert num_position("ha8ityjgkaw jyocvv56qe15yjdc9av6fot9db8") == 2
assert num_position("wmvdw5v7h8ns fzcl1umy7yhplu7y3gaj09e") == 5
assert num_position("833621sfvb7 o672z2qzatnaeknwbyl1yy44 k") == 0
assert num_position("5wvmzd togk y24saio0ddwa edfyqyillx") == 0
assert num_position("4hf1oly40nkkac ce3q 8tmlokkvwa") == 0
assert num_position("z27t5tgzyn6ar7oytrvmtf655o98tqr02i4") == 1
assert num_position("h1 cmcfbc2k80upvbvmoi81qap ulauah6fpy2 ") == 1
assert num_position("9u dm7ffnnpvdapc8nqphofim0ivrjxk") == 0
assert num_position("3wbdppff1brvgrmievk2takm6 zf m") == 0
assert num_position("7pjib1dqhhqrqzob6rwnkr1gust3bezat") == 0
assert num_position("bjwem1j08 v7gbc aotvcruzsvejx99vpjkx2l") == 5
assert num_position("jz9fsp0yluv2p1mmylwbuincnlfqhjrqc7") == 2
assert num_position("3gyr4yaq6uolklsc93d6js58cjaa8f") == 0
assert num_position("0w8i0dkblx9g03p123awj0mqb39a5efe1p") == 0
assert num_position("weylzblvcyi5vjeia316r0v922z6ic") == 11
assert num_position("3gtmcaygyb2ncfxytiaysjv72jx27u0rl") == 0
assert num_position("pn efsxk39dzer6nj92oafv3iju3ue") == 8
assert num_position("mafy7992f 3hkxbg6i3q904eowft2ow ") == 4
assert num_position("9o5ucvqjvs2qu8404yqrgzcreqhkxvop") == 0
assert num_position("qwd8delx8hfbaechjszoio7ndbkgyhddfdu9dw5") == 3
assert num_position("w3m58kdjiv7sce2vrh76 5hm42husf7x17j30rl") == 1
assert num_position(" jjnbz cu feimytxhmt0syab0rye5m") == 20