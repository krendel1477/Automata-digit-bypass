
class StatesTable:
    def __init__ (self):
        self.first_start_program = {
            ("q0",frozenset({"n", "e"})) : ["right", "q0"],
            ("q0",frozenset({"n", "e", "w"})) : ["right", "q0"],
            ("q0",frozenset({"n", "e", "w", "s"})) : ["right", "q0"],
            ("q0",frozenset({"n", "e", "s"})) : ["right", "q0"],
            ("q0",frozenset({"n", "w"})) : ["up", "q1"],
            ("q0",frozenset({"n", "w", "s"})) : ["up", "q1"],
            ("q1",frozenset({"s", "w", "n"})) : ["left", "q1"],
            ("q1",frozenset({"s", "w", "n", "e"})) : ["left", "q1"],
            ("q1",frozenset({"s", "e", "n"})) : ["up", "q0"],
            ("q1",frozenset({"s", "w", "e"})) : ["left", "q10"], # new 1 (2-е поколение) для 1
            ("q0",frozenset({"s", "w", "e"})) : ["left", "q10"] #new 1 (2-е поколение) для 1
        }

        self.third_start_program = {
            ("q0",frozenset({"n", "e"})) : ["right", "q0"],
            ("q0",frozenset({"n", "e", "w"})) : ["right", "q0"],
            ("q0",frozenset({"n", "e", "w", "s"})) : ["right", "q0"],
            ("q0",frozenset({"n", "e", "s"})) : ["right", "q0"],
            ("q0",frozenset({"n", "w"})) : ["up", "q1"],
            ("q0",frozenset({"n", "w", "s"})) : ["up", "q1"],
            ("q1",frozenset({"s", "w", "n"})) : ["left", "q1"],
            ("q1",frozenset({"s", "w", "n", "e"})) : ["left", "q1"],
            ("q1",frozenset({"s", "e", "n"})) : ["up", "q0"],
            ("q1",frozenset({"s", "w", "e"})) : ["right", "q10"], # new 3 (2-е поколение) для 3
            ("q0",frozenset({"s", "w", "e"})) : ["right", "q10"] #new 3 (2-е поколение) для 3
        }

        self.first_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["left", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s", "w"})) : ["left", "q10"],
            ("q10",frozenset({"s"})) : ["down", "q100"], # удалить если точность падает
            ("q100",frozenset({"s", "w", "e", "n"})) : ["left", "q10"], # удалить если точность падает
            ("q10",frozenset({"s", "w", "n"})) : ["up", "q11"],
            ("q11",frozenset({"s", "w", "n"})) : ["up", "q11"],
            ("q11",frozenset({"s", "w"})) : ["left", "q10"],
            ("q11",frozenset({"s", "w", "e"})) : ["left", "q10"],
            ("q11",frozenset({"s", "w", "n", "e"})) : ["right", "q11"],
            ("q11",frozenset({"n", "w"})) : ["up", "q11"],
            ("q11",frozenset({"n", "w", "e"})) : ["right", "q12"],
            ("q12",frozenset({"n", "w", "e"})) : ["right", "q12"],
            ("q12",frozenset({"n", "w", "e", "s"})) : ["down", "q12"],
            ("q12",frozenset({"n", "e"})) : ["right", "q12"],
            ("q12",frozenset({"n", "s", "e"})) : ["down", "q13"],
            ("q12",frozenset({"n", "w"})) : ["up", "q120"],
            ("q12",frozenset({"n"})) : ["up", "q120"],
            ("q120",frozenset({"n", "w", "e", "s"})) : ["right", "q12"],
            ("q13",frozenset({"n", "e"})) : ["right", "q12"],
            ("q13",frozenset({"n", "s", "e"})) : ["down", "q13"],
            ("q13",frozenset({"n", "w", "e"})) : ["right", "q13"],
            ("q13",frozenset({"n", "s", "e", "w"})) : ["left", "q13"],
            ("q13",frozenset({"s", "e"})) : ["down", "q13"],
            ("q13",frozenset({"s", "e", "w"})) : ["left", "q13"]
            # ("q14",frozenset({"s", "e", "w", "n"})) : ["right", "q14"],
            # ("q14",frozenset({"s", "w", "n"})) : ["up", "q14"]
        }

        self.second_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s", "e", "n"})) : ["up", "q11"], # new 2 (3-е поколение) q10
            ("q10",frozenset({"s", "e"})) : ["right", "q11"],
            ("q11",frozenset({"s", "w"})) : ["down", "q18"], # new 2 (3- поколение) жесткий экстрамув
            ("q11",frozenset({"s", "e", "n"})) : ["up", "q11"], # new 2 (3-е поколение)
            ("q11",frozenset({"s", "e"})) : ["right", "q11"], # new 2 (3-е поколение)
            ("q11",frozenset({"s", "e", "w"})) : ["right", "q11"], # new 2 (3-е поколение) q10
            ("q11",frozenset({"s", "e", "n", "w"})) : ["up", "q11"],
            ("q11",frozenset({"s", "e", "n"})) : ["up", "q12"],
            ("q12",frozenset({"s"})) : ["down", "q999"], # new 2 (6-е поколение)
            ("q999",frozenset({"n", "s", "e"})) : ["right", "q999"], # new 2 (6-е поколение)
            ("q999",frozenset({"w", "s"})) : ["down", "q999"], # new 2 (6-е поколение)
            ("q999",frozenset({"w", "s", "e", "n"})) : ["right", "q999"], # new 2 (6-е поколение)
            ("q999",frozenset({"w", "s", "e"})) : ["right", "q10"], # new 2 (6-е поколение)
            ("q12",frozenset({"s", "e", "n"})) : ["up", "q12"],
            ("q12",frozenset({"s", "e", "n", "w"})) : ["left", "q12"],
            ("q12",frozenset({"s", "e", "w"})) : ["left", "q12"], # new 2 (3-е поколение)
            ("q12",frozenset({"e", "w"})) : ["left", "q102"], # new 2 (3-е поколение)
            ("q102",frozenset({"e", "w"})) : ["left", "q102"], # new 2 (3-е поколение)
            ("q102",frozenset({"s", "e", "w"})) : ["down", "q13"], # new 2 (3-е поколение)
            ("q12",frozenset({"e", "n"})) : ["up", "q12"],
            ("q12",frozenset({"e"})) : ["right", "q11"], # new 2 (5-е поколение)
            ("q12",frozenset({"e", "s"})) : ["right", "q11"],
            ("q12",frozenset({"e", "n", "w"})) : ["left", "q13"],
            ("q13",frozenset({"e"})) : ["right", "q999"], # new 2 (6-е поколение)
            ("q999",frozenset({"e", "n", "w"})) : ["up", "q999"], # new 2 (6-е поколение)
            ("q999",frozenset({"s", "n", "w"})) : ["down", "q999"], # new 2 (6-е поколение)
            ("q13",frozenset({"e", "n", "w"})) : ["left", "q13"],
            ("q13",frozenset({"e", "n", "s"})) : ["up", "q15"], # new 2 (3-е поколение)
            ("q13",frozenset({"e", "n", "w", "s"})) : ["down", "q13"],
            ("q13",frozenset({"n", "w", "s"})) : ["down", "q13"],
            ("q13",frozenset({"n", "w"})) : ["left", "q13"],
            ("q13",frozenset({"n", "s"})) : ["up", "q103"], # new 2 (4-е поколение)
            ("q103",frozenset({"w", "n", "s"})) : ["left", "q13"], # new 2 (4-е поколение)
            ("q13",frozenset({"n"})) : ["up", "q15"], # new 2 (2-е поколение)
            ("q13",frozenset({"n", "e"})) : ["up", "q14"],
            ("q14",frozenset({"w", "e", "s"})) : ["left", "q102"], # new 2 (4-е поколение)
            ("q14",frozenset({"n", "e", "s"})) : ["up", "q15"],
            ("q15",frozenset({"n", "e", "s"})) : ["up", "q15"],
            ("q15",frozenset({"n", "e", "s", "w"})) : ["left", "q14"],
            ("q14",frozenset({"n", "e", "w"})) : ["left", "q14"],
            ("q14",frozenset({"n", "e"})) : ["up", "q15"],
            ("q14",frozenset({"n", "e", "s", "w"})) : ["down", "q14"],
            ("q14",frozenset({"n", "s", "w"})) : ["down", "q14"],
            ("q14",frozenset({"n", "w"})) : ["left", "q106"],
            ("q106",frozenset({"n", "w", "e"})) : ["left", "q106"],
            ("q106",frozenset({"n", "w"})) : ["left", "q106"],
            ("q106",frozenset({"n", "w", "e", "s"})) : ["down", "q106"],
            ("q106",frozenset({"n", "e"})) : ["up", "q15"],
            ("q106",frozenset({"n", "s", "w"})) : ["down", "q16"],
            ("q16",frozenset({"n", "s", "w"})) : ["down", "q16"],
            ("q16",frozenset({"n", "w", "e", "s"})) : ["right", "q16"],
            ("q16",frozenset({"w", "s"})) : ["down", "q16"], # new 2 (2-е поколение)
            ("q16",frozenset({"w", "n"})) : ["left", "q106"], # new 2 (3-е поколение)
            ("q16",frozenset({"s", "w", "e"})) : ["right", "q17"],
            ("q17",frozenset({"s", "w", "e"})) : ["right", "q17"],
            ("q17",frozenset({"n", "w", "e", "s"})) : ["up", "q17"],
            ("q17",frozenset({"n", "e", "s"})) : ["up", "q17"],
            ("q17",frozenset({"e", "s"})) : ["right", "q17"],
            ("q17",frozenset({"s"})) : ["down", "q107"],
            ("q107",frozenset({"n", "w", "e", "s"})) : ["right", "q17"],
            ("q17",frozenset({"w", "s"})) : ["down", "q18"],
            ("q17",frozenset({"n", "w", "s"})) : ["down", "q18"],
            ("q18",frozenset({"n", "s", "w"})) : ["down", "q18"],
            ("q18",frozenset({"n", "w"})) : ["left", "q108"], # new 2 (4-е поколение)
            ("q18",frozenset({"n", "s", "w", "e"})) : ["right", "q18"],
            ("q18",frozenset({"w", "s"})) : ["down", "q18"],
            ("q18",frozenset({"w"})) : ["left", "q108"],
            ("q108",frozenset({"n", "s", "w", "e"})) : ["down", "q18"],
            ("q108",frozenset({"s", "w", "e"})) : ["down", "q18"],
            ("q18",frozenset({"s", "w", "e"})) : ["right", "q18"],
        }
        
        self.third_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "w", "n"})) : ["down", "q11"], # new 3 (2-е поколение)
            ("q10",frozenset({"s", "e"})) : ["right", "q10"], # new 3 (3-е поколение)
            ("q10",frozenset({"s", "n"})) : ["down", "q11"], # new 3 (4-е поколение)
            ("q10",frozenset({"s", "w"})) : ["down", "q11"], # new 3 (3-е поколение)
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s"})) : ["down", "q11"],
            ("q11",frozenset({"s", "e", "n"})) : ["right", "q11"],
            ("q11",frozenset({"s", "w"})) : ["down", "q11"],
            ("q11",frozenset({"s", "w", "e", "n"})) : ["right", "q11"],
            ("q11",frozenset({"s", "w", "n"})) : ["down", "q11"],
            ("q11",frozenset({"s", "w", "e"})) : ["right", "q12"],
            ("q12",frozenset({"s", "w", "e"})) : ["right", "q12"],
            ("q12",frozenset({"s"})) : ["down", "q13"], # new 3 (2-е поколение)
            ("q12",frozenset({"s", "w", "e", "n"})) : ["up", "q12"],
            ("q12",frozenset({"s", "n", "e"})) : ["up", "q12"],
            ("q12",frozenset({"s", "e"})) : ["right", "q12"],
            ("q12",frozenset({"s", "w", "n"})) : ["down", "q15"],
            ("q12",frozenset({"s", "w"})) : ["down", "q13"],
            ("q13",frozenset({"s", "w"})) : ["down", "q13"],
            ("q13",frozenset({"s", "w", "e"})) : ["right", "q103"], # new 3 (3-е поколение)
            ("q103",frozenset({"s", "w"})) : ["down", "q103"], # new 3 (3-е поколение)
            ("q103",frozenset({"s", "w", "e", "n"})) : ["right", "q103"], # new 3 (3-е поколение)
            ("q103",frozenset({"s", "w", "n"})) : ["down", "q13"], # new 3 (3-е поколение)
            ("q103",frozenset({"s", "w", "e"})) : ["right", "q14"], # new 3 (3-е поколение)
            ("q13",frozenset({"s", "e", "n"})) : ["right", "q15"], # new 3 (2-е поколение)
            ("q13",frozenset({"s", "n", "w"})) : ["down", "q13"],
            ("q13",frozenset({"s", "n", "w", "e"})) : ["right", "q13"],
            ("q13",frozenset({"n", "w"})) : ["left", "q14"],
            ("q14",frozenset({"s", "w", "e"})) : ["right", "q16"], # new 3 (3-е поколение)
            ("q14",frozenset({"s", "w", "n"})) : ["up", "q14"], # new 3 (3-е поколение)
            ("q14",frozenset({"s", "n"})) : ["up", "q1004"], # new 3 (3-е поколение)
            ("q1004",frozenset({"s", "n"})) : ["up", "q1004"], # new 3 (3-е поколение)
            ("q1004",frozenset({"s", "n", "w"})) : ["left", "q17"], # new 3 (3-е поколение)
            ("q14",frozenset({"n", "w"})) : ["left", "q14"],
            ("q14",frozenset({"n", "w", "e"})) : ["left", "q14"],
            ("q14",frozenset({"n", "w", "e", "s"})) : ["down", "q104"],
            ("q104",frozenset({"n", "w", "e", "s"})) : ["up", "q104"],
            ("q104",frozenset({"n", "e", "s"})) : ["up", "q14"],
            ("q14",frozenset({"n", "e", "s"})) : ["up", "q14"],
            ("q14",frozenset({"e", "s"})) : ["right", "q14"],
            ("q104",frozenset({"n", "w", "s"})) : ["down", "q15"],
            ("q104",frozenset({"n", "w"})) : ["left", "q14"],
            ("q15",frozenset({"n", "w", "s"})) : ["down", "q15"],
            ("q15",frozenset({"n", "w"})) : ["left", "q14"],
            ("q15",frozenset({"n", "w", "e", "s"})) : ["right", "q15"],
            ("q15",frozenset({"w", "s"})) : ["down", "q15"],
            ("q15",frozenset({"w", "e", "s"})) : ["right", "q16"],
            ("q16",frozenset({"w", "e", "s"})) : ["right", "q16"],
            ("q16",frozenset({"w", "s"})) : ["down", "q13"], # new 3 (4-е поколение)
            ("q16",frozenset({"w", "e", "s", "n"})) : ["up", "q16"],
            ("q16",frozenset({"e", "s"})) : ["right", "q16"],
            ("q16",frozenset({"e", "s", "n"})) : ["up", "q17"],
            ("q17",frozenset({"e", "s", "n"})) : ["up", "q17"],
            ("q17",frozenset({"e", "s"})) : ["right", "q16"], # new 3 (2-е поколение)
            ("q17",frozenset({"e", "s", "n", "w"})) : ["left", "q17"],
            ("q17",frozenset({"e", "n"})) : ["up", "q17"],
            ("q17",frozenset({"e", "n", "w"})) : ["left", "q18"],
            ("q18",frozenset({"e", "n", "w"})) : ["left", "q18"],
            ("q18",frozenset({"e", "n"})) : ["up", "q108"],
            ("q108",frozenset({"e", "n", "w", "s"})) : ["left", "q108"],
            ("q108",frozenset({"e", "n", "w"})) : ["left", "q19"],
            ("q18",frozenset({"e", "n", "w", "s"})) : ["down", "q18"],
            ("q18",frozenset({"n", "w"})) : ["left", "q18"],
            ("q18",frozenset({"n"})) : ["up", "q108"], # new 3 (2-е поколение)
            ("q108",frozenset({"n", "w", "s"})) : ["left", "q108"], # new 3 (2-е поколение)
            ("q108",frozenset({"n", "e"})) : ["up", "q19"], # new 3 (2-е поколение)
            ("q18",frozenset({"s", "n", "w"})) : ["down", "q18"],
            ("q108",frozenset({"s", "n", "e"})) : ["up", "q19"],
            ("q19",frozenset({"s", "n", "e", "w"})) : ["left", "q19"],
            ("q19",frozenset({"n", "e"})) : ["up", "q19"],
            ("q19",frozenset({"n", "e", "w"})) : ["left", "q20"],
            ("q20",frozenset({"n"})) : ["up", "q108"],
            ("q20",frozenset({"s", "n", "e", "w"})) : ["right", "q20"],
            ("q20",frozenset({"w", "n", "e"})) : ["left", "q200"],
            ("q200",frozenset({"w", "n", "e"})) : ["left", "q200"],
            ("q200",frozenset({"n", "e"})) : ["up", "q108"],
            ("q20",frozenset({"w", "n", "s"})) : ["down", "q20"],
            ("q20",frozenset({"w", "n"})) : ["left", "q200"],
            ("q200",frozenset({"w", "n", "s", "e"})) : ["down", "q20"],
            ("q20",frozenset({"w", "s"})) : ["down", "q20"],
            ("q20",frozenset({"w", "e", "s"})) : ["right", "q20"],
        }

        self.inverted_third_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s"})) : ["down", "q18"], # new 3 (6-е поколение)
            ("q10",frozenset({"s", "w"})) : ["down", "q18"], # new 3 (8-е поколение)
            ("q10",frozenset({"s", "e"})) : ["right", "q10"], # new 3 (3-е поколение)
            ("q10",frozenset({"s", "w", "n"})) : ["up", "q10"], # new 3 (5-е поколение)
            ("q10",frozenset({"s", "n"})) : ["up", "q100"], # new 3 (5-е поколение)
            ("q100",frozenset({"s", "n"})) : ["up", "q100"], # new 3 (5-е поколение)
            ("q100",frozenset({"s"})) : ["down", "q18"], # new 3 (5-е поколение)
            ("q18",frozenset({"s", "n"})) : ["down", "q18"], # new 3 (5-е поколение)
            ("q100",frozenset({"s", "n", "w"})) : ["left", "q11"], # new 3 (5-е поколение)
            ("q10",frozenset({"s", "e", "n"})) : ["up", "q11"],
            ("q11",frozenset({"s", "e", "w"})) : ["right", "q18"],
            ("q11",frozenset({"s", "e"})) : ["right", "q10"],
            ("q11",frozenset({"e"})) : ["right", "q17"],
            ("q11",frozenset({"s"})) : ["down", "q18"], #new 3 (6-поколение)
            ("q11",frozenset({"s", "e", "n"})) : ["up", "q11"],
            ("q11",frozenset({"s", "w", "e", "n"})) : ["left", "q11"],
            ("q11",frozenset({"e", "n"})) : ["up", "q11"],
            ("q11",frozenset({"w", "e", "n"})) : ["left", "q12"],
            ("q12",frozenset({"w", "e", "n"})) : ["left", "q12"],
            ("q12",frozenset({"s", "w", "e", "n"})) : ["down", "q12"],
            ("q12",frozenset({"w", "n"})) : ["left", "q12"],
            ("q12",frozenset({"w", "n", "s"})) : ["left", "q13"], # new 3 (5-поколение)
            ("q12",frozenset({"n"})) : ["up", "q13"], # new 3 (2-е поколение)
            ("q12",frozenset({"s", "n"})) : ["up", "q13"], # new 3 (8-поколение)
            ("q12",frozenset({"e", "n", "s"})) : ["up", "q13"], # new 3 (5-е поколение)
            ("q12",frozenset({"e", "n"})) : ["up", "q13"],
            ("q13",frozenset({"s", "e", "n"})) : ["up", "q13"],
            ("q13",frozenset({"s", "e"})) : ["right", "q18"], # new (9-е поколение)
            ("q13",frozenset({"s", "w", "e", "n"})) : ["left", "q13"],
            ("q13",frozenset({"s", "w", "e"})) : ["right", "q13"], # new 3 (3-е поколение)
            ("q13",frozenset({"e", "n"})) : ["up", "q13"],
            ("q13",frozenset({"w", "s"})) : ["down", "q20"], # new 3 (3-е поколение)
            ("q13",frozenset({"w", "n", "s"})) : ["left", "q14"], # new 3 (4-е поколение)
            ("q13",frozenset({"w", "e", "n"})) : ["left", "q14"],
            ("q14",frozenset({"e", "n"})) : ["up", "q13"], # new 3 (3-е поколение)
            ("q14",frozenset({"n"})) : ["up", "q13"], # new 3 (2-е поколение)
            ("q14",frozenset({"w", "e", "n"})) : ["left", "q14"],
            ("q14",frozenset({"s", "e", "n"})) : ["up", "q13"], # new 3 (8-е поколение)
            ("q14",frozenset({"s", "w", "e", "n"})) : ["down", "q14"],
            ("q14",frozenset({"w", "n"})) : ["left", "q14"],
            ("q14",frozenset({"s", "w", "n"})) : ["down", "q15"],
            ("q15",frozenset({"w", "n"})) : ["left", "q15"],
            ("q15",frozenset({"n"})) : ["up", "q13"], # new 3 (5-е поколение)
            ("q15",frozenset({"n", "e"})) : ["up", "q13"], # new 3 (7-е поколение)
            ("q15",frozenset({"e", "w", "n"})) : ["left", "q13"],
            ("q15",frozenset({"s", "w", "n"})) : ["down", "q15"],
            ("q15",frozenset({"w", "n", "e", "s"})) : ["down", "q16"],
            ("q16",frozenset({"s", "w", "n"})) : ["down", "q16"],
            ("q16",frozenset({"s", "e", "n"})) : ["right", "q18"],
            ("q16",frozenset({"s", "w"})) : ["down", "q16"],
            ("q16",frozenset({"n", "w"})) : ["left", "q15"], # new 3 (4-е поколение)
            ("q16",frozenset({"w", "n", "e", "s"})) : ["right", "q16"],
            ("q16",frozenset({"s", "w", "e"})) : ["right", "q17"],
            ("q17",frozenset({"s", "w", "n"})) : ["down", "q16"], # new 3 (4-е поколение)
            ("q17",frozenset({"s", "w", "e"})) : ["right", "q17"],
            ("q17",frozenset({"s", "w", "e", "n"})) : ["up", "q17"],
            ("q17",frozenset({"s", "n", "e"})) : ["up", "q17"],
            ("q17",frozenset({"s", "e"})) : ["right", "q17"],
            ("q17",frozenset({"s", "w"})) : ["down", "q18"],
            ("q17",frozenset({"s"})) : ["down", "q18"], # new 3 (2-е поколение)
            ("q17",frozenset({"n", "s"})) : ["down", "q18"], # new 3 (3-е поколение)
            ("q18",frozenset({"n", "e", "s"})) : ["right", "q18"],
            ("q18",frozenset({"s", "w", "e", "n"})) : ["right", "q18"],
            ("q18",frozenset({"s", "w"})) : ["down", "q18"],
            ("q18",frozenset({"s", "w", "n"})) : ["down", "q18"],
            ("q18",frozenset({"n", "w"})) : ["left", "q120"], # new 3 (4-е поколение)
            ("q18",frozenset({"w"})) : ["left", "q120"], # new 3 (4-е поколение)
            ("q18",frozenset({"n"})) : ["up", "q120"], # new 3 (4-е поколение)
            ("q120",frozenset({"n", "s", "w"})) : ["left", "q120"], # new 3 (4-е поколение)
            ("q18",frozenset({"s", "w", "e"})) : ["right", "q19"],
            ("q19",frozenset({"s", "w", "e"})) : ["right", "q19"],
            ("q19",frozenset({"s", "w", "e", "n"})) : ["up", "q19"],
            ("q19",frozenset({"s", "e", "n"})) : ["up", "q19"],
            ("q19",frozenset({"s", "w", "n"})) : ["down", "q20"],
            ("q19",frozenset({"s", "e"})) : ["right", "q19"],
            ("q19",frozenset({"s", "w"})) : ["down", "q20"],
            ("q19",frozenset({"s"})) : ["down", "q20"], # new 3 (2-е поколение)
            ("q20",frozenset({"s", "w"})) : ["down", "q20"],
            ("q20",frozenset({"n", "w"})) : ["left", "q120"], # new 3 (2-е поколение)
            ("q120",frozenset({"n", "w", "e"})) : ["left", "q120"], # new 3 (2-е поколение)
            ("q120",frozenset({"n", "e"})) : ["up", "q2000"], # new 3 (2-е поколение)
            ("q120",frozenset({"n", "w", "e", "s"})) : ["down", "q20"], # new 3 (2-е поколение)
            ("q20",frozenset({"n", "w", "e"})) : ["left", "q120"], # new 3 (2-е поколение)
            ("q20",frozenset({"s", "w", "n"})) : ["down", "q20"],
            ("q20",frozenset({"s", "w", "e", "n"})) : ["right", "q20"],
            ("q20",frozenset({"w"})) : ["left", "q120"],
            ("q20",frozenset({"n"})) : ["up", "q2000"],
            ("q2000",frozenset({"n", "w", "s", "e"})) : ["left", "q120"],
            ("q20",frozenset({"s", "e", "n"})) : ["right", "q10"],
            ("q20",frozenset({"s", "w", "e"})) : ["right", "q200"],
            ("q200",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q200",frozenset({"s", "w"})) : ["down", "q20"],
            # ("q200",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            
            # ("q200",frozenset({"s", "w"})) : ["down", "q13"],
        }

        self.fourth_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "n", "e"})) : ["up", "q11"],
            ("q11",frozenset({"s", "n", "e"})) : ["up", "q11"],
            ("q11",frozenset({"w", "n", "e"})) : ["up", "q14"], # new 4 (5-е поколение)
            ("q11",frozenset({"s", "n", "e", "w"})) : ["left", "q11"],
            ("q11",frozenset({"n", "e"})) : ["up", "q11"],
            ("q11",frozenset({"s"})) : ["down", "q102"], # new 4 (6-е поколение)
            ("q11",frozenset({"e"})) : ["right", "q12"], # new 4 (5-е поколение)
            ("q11",frozenset({"s", "w", "e"})) : ["right", "q12"],
            ("q11",frozenset({"s", "e"})) : ["right", "q12"], # new 4 (2-е поколение)
            ("q12",frozenset({"s", "w", "e"})) : ["right", "q12"],
            ("q12",frozenset({"s", "w", "e", "n"})) : ["up", "q13"],
            ("q13",frozenset({"s"})) : ["down", "q102"],
            ("q102",frozenset({"s", "w", "e", "n"})) : ["right", "q12"],
            ("q102",frozenset({"s", "e", "n"})) : ["right", "q12"],
            ("q102",frozenset({"s", "w", "n"})) : ["down", "q102"],
            ("q12",frozenset({"s", "w"})) : ["down", "q102"],
            ("q12",frozenset({"s", "w", "n"})) : ["up", "q13"], # new 4 (6-е поколение)
            ("q13",frozenset({"s", "n"})) : ["up", "q13"], # new 4 (6-е поколение)
            ("q13",frozenset({"s", "w", "n"})) : ["left", "q14"], # new 4 (6-е поколение)
            ("q13",frozenset({"s", "e", "n"})) : ["up", "q13"],
            ("q13",frozenset({"s", "e"})) : ["right", "q12"], # new 4 (2-е поколение)
            ("q13",frozenset({"s", "w", "e", "n"})) : ["left", "q14"],
            ("q14",frozenset({"w", "e", "n"})) : ["left", "q14"],
            ("q14",frozenset({"n"})) : ["up", "q104"], # new 4 (5-е поколение)
            ("q104",frozenset({"s", "e", "n"})) : ["up", "q11"], # new 4 (3-е поколение)
            ("q14",frozenset({"e", "n"})) : ["up", "q104"],
            ("q104",frozenset({"s", "w", "e", "n"})) : ["left", "q14"],
            ("q104",frozenset({"s", "w", "e"})) : ["left", "q14"],
            ("q14",frozenset({"w", "e"})) : ["left", "q14"],
            ("q14",frozenset({"s", "w", "e"})) : ["down", "q14"],
            ("q14",frozenset({"w", "n"})) : ["left", "q14"],
            ("q14",frozenset({"s", "w", "e", "n"})) : ["down", "q14"],
            ("q14",frozenset({"s", "w", "n"})) : ["down", "q15"],
            ("q15",frozenset({"s", "w", "n"})) : ["down", "q15"],
            ("q15",frozenset({"n", "e"})) : ["up", "q104"], # new 4 (8-е поколение)
            ("q15",frozenset({"n"})) : ["up", "q104"], # new 4 (6-е поколение)
            ("q104",frozenset({"n", "s", "w"})) : ["left", "q14"], # new 4 (6-е поколение)
            ("q104",frozenset({"s", "e"})) : ["right", "q12"], # new 4 (7-е поколение)
            ("q15",frozenset({"s", "w", "e", "n"})) : ["right", "q15"],
            ("q15",frozenset({"s", "w", "e"})) : ["right", "q15"],
            ("q15",frozenset({"s", "w"})) : ["down", "q15"],
            ("q15",frozenset({"w"})) : ["left", "q106"], # new 4 (2-е поколение)
            ("q15",frozenset({"n", "w", "e"})) : ["left", "q16"], # new 4 (6-е поколение)
            ("q15",frozenset({"n", "w"})) : ["left", "q16"],
            ("q16",frozenset({"n", "w"})) : ["left", "q16"],
            ("q16",frozenset({"n", "e"})) : ["up", "q104"], # new 4 (7-е поколение)
            ("q16",frozenset({"n", "w", "e"})) : ["left", "q16"],
            ("q106",frozenset({"n", "w", "e", "s"})) : ["down", "q106"], # new 4 (2-е поколение)
            ("q106",frozenset({"n", "w"})) : ["left", "q106"], # new 4 (2-е поколение)
            ("q106",frozenset({"n", "w", "e"})) : ["left", "q106"],
            ("q106",frozenset({"s", "w", "e"})) : ["down", "q15"], # new 4 (8-е поколение)
            ("q106",frozenset({"n", "w", "s"})) : ["down", "q16"],
            ("q106",frozenset({"n"})) : ["up", "q1006"],
            ("q1006",frozenset({"n", "w", "e", "s"})) : ["left", "q106"], # new 4 (4-е поколение)
            ("q106",frozenset({"n", "e"})) : ["up", "q1006"], # new 4 (4-е поколение)
            ("q16",frozenset({"n", "w", "s"})) : ["down", "q16"],
            ("q16",frozenset({"n", "w", "e", "s"})) : ["right", "q17"],
            ("q17",frozenset({"n", "w", "e"})) : ["left", "q106"], # new 4 (3-е поколение)
            ("q17",frozenset({"n", "w"})) : ["left", "q106"], # new 4 (4-е поколение)
            ("q17",frozenset({"n", "w", "s"})) : ["down", "q17"],
            ("q17",frozenset({"n", "w", "e", "s"})) : ["right", "q17"],
            ("q17",frozenset({"w", "e", "s"})) : ["right", "q17"],
            ("q17",frozenset({"w", "s"})) : ["down", "q17"],
        }

        self.fifth_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s", "e"})) : ["right", "q10"], # new 5 (2-е поколение)
            ("q10",frozenset({"s", "e", "n"})) : ["up", "q11"],
            ("q11",frozenset({"s", "e"})) : ["right", "q10"], # new 5 (3-е поколение)
            ("q11",frozenset({"s", "e", "n"})) : ["up", "q11"],
            ("q11",frozenset({"s", "w", "e", "n"})) : ["left", "q11"],
            ("q11",frozenset({"e", "n"})) : ["up", "q11"],
            ("q11",frozenset({"w", "e", "n"})) : ["left", "q12"],
            ("q12",frozenset({"w", "e", "n"})) : ["left", "q12"],
            ("q12",frozenset({"w", "e"})) : ["right", "q102"],
            ("q102",frozenset({"w", "e", "n"})) : ["up", "q11"],
            ("q12",frozenset({"n"})) : ["up", "q13"], # new 5 (3-е поколение)
            ("q12",frozenset({"s", "w", "e", "n"})) : ["down", "q12"],
            ("q12",frozenset({"w", "n"})) : ["left", "q12"],
            ("q12",frozenset({"s", "n"})) : ["up", "q13"],
            ("q12",frozenset({"w", "n", "s"})) : ["down", "q12"],
            ("q12",frozenset({"n", "e"})) : ["up", "q13"],
            ("q12",frozenset({"s", "e", "n"})) : ["up", "q13"], # new 5 (3-е поколение)
            ("q13",frozenset({"n", "e"})) : ["up", "q13"],
            ("q13",frozenset({"n", "e", "s"})) : ["up", "q13"],
            ("q13",frozenset({"w", "n", "e", "s"})) : ["left", "q13"],
            ("q13",frozenset({"w", "n", "s"})) : ["left", "q13"], # new 5 (3-е поколение)
            ("q13",frozenset({"w", "n", "e"})) : ["left", "q103"],
            ("q13",frozenset({"w", "s", "e"})) : ["left", "q103"], # new 5 (2-е поколение)
            ("q13",frozenset({"s", "e"})) : ["right", "q1004"], # new 5 (5-е поколение)
            ("q1004",frozenset({"w", "n", "s", "e"})) : ["up", "q13"], # new 5 (5-е поколение)
            ("q103",frozenset({"w", "e"})) : ["left", "q103"], # new 5 (2-е поколение)
            ("q103",frozenset({"w", "s", "e"})) : ["down", "q14"], # new 5 (2-е поколение)
            ("q103",frozenset({"w", "n", "e"})) : ["left", "q103"],
            ("q103",frozenset({"e"})) : ["right", "q1004"], # new 5 (6-е поколение)
            ("q1004",frozenset({"e", "w", "n"})) : ["up", "q1004"], # new 5 (6-е поколение)
            ("q1004",frozenset({"e", "s", "n"})) : ["up", "q13"], # new 5 (6-е поколение)
            ("q103",frozenset({"n", "e"})) : ["up", "q13"], # new 5 (3-е поколение)
            ("q103",frozenset({"w", "n", "e", "s"})) : ["down", "q14"],
            ("q14",frozenset({"w", "n", "s"})) : ["down", "q14"],
            ("q14",frozenset({"w", "n", "e", "s"})) : ["right", "q14"],
            ("q14",frozenset({"w"})) : ["left", "q103"],
            ("q14",frozenset({"w", "n"})) : ["left", "q104"], # new 5 (3-е поколение)
            ("q14",frozenset({"s", "n"})) : ["up", "q13"], # new 5 (3-е поколение)
            ("q104",frozenset({"s", "e", "w", "n"})) : ["down", "q14"], # new 5 (3-е поколение)
            ("q104",frozenset({"s", "e", "n"})) : ["up", "q13"], # new 5 (5-е поколение)
            ("q104",frozenset({"w", "e", "n"})) : ["left", "q12"], # new 5 (5-е поколение)
            ("q104",frozenset({"e", "n"})) : ["up", "q13"], # new 5 (5-е поколение)
            ("q14",frozenset({"w", "s"})) : ["down", "q14"], # new 5 (3-е поколение)
            ("q14",frozenset({"n"})) : ["up", "q13"], # new 5 (5-е поколение)
            ("q14",frozenset({"e", "w", "s"})) : ["down", "q15"],
            ("q15",frozenset({"e", "w", "s"})) : ["right", "q15"],
            ("q15",frozenset({"w", "s"})) : ["down", "q105"], # new 5 (3-е поколение)
            ("q15",frozenset({"w", "n", "e"})) : ["left", "q1005"], # new 5 (5-е поколение)
            ("q1005",frozenset({"w", "n", "s"})) : ["left", "q16"], # new 5 (5-е поколение)
            ("q15",frozenset({"w", "n"})) : ["left", "q1005"], # new 5 (3-е поколение)
            ("q1005",frozenset({"w", "n"})) : ["left", "q1005"], # new 5 (3-е поколение)
            ("q1005",frozenset({"w", "n", "e", "s"})) : ["down", "q14"], # new 5 (3-е поколение)
            ("q1005",frozenset({"w", "s", "e"})) : ["down", "q1005"], # new 5 (3-е поколение)
            ("q105",frozenset({"w", "s"})) : ["down", "q105"], # new 5 (3-е поколение)
            ("q105",frozenset({"n", "w", "s"})) : ["down", "q105"], # new 5 (3-е поколение)
            ("q105",frozenset({"w", "s", "e", "n"})) : ["right", "q15"], # new 5 (3-е поколение)
            ("q105",frozenset({"w", "n"})) : ["left", "q16"], # new 5 (3-е поколение)
            # ("q105",frozenset({"e", "w", "s"})) : ["down", "q15"], # new 5 (3-е поколение)
            ("q15",frozenset({"n", "e", "w", "s"})) : ["up", "q15"],
            ("q15",frozenset({"n", "e", "s"})) : ["up", "q15"],
            ("q15",frozenset({"e", "s"})) : ["right", "q15"],
            ("q15",frozenset({"s"})) : ["down", "q16"],
            ("q15",frozenset({"w"})) : ["left", "q1006"], # new 5 (5-е поколение)
            ("q15",frozenset({"w", "s", "n"})) : ["down", "q16"],
            ("q16",frozenset({"w", "s", "n"})) : ["down", "q16"],
            ("q16",frozenset({"e", "s", "n"})) : ["right", "q16"], # new 5 (3-е поколение)
            ("q16",frozenset({"w", "n"})) : ["left", "q106"],
            ("q16",frozenset({"n"})) : ["up", "q1006"],
            ("q106",frozenset({"w", "e", "n"})) : ["left", "q106"],
            ("q106",frozenset({"s", "e", "n"})) : ["up", "q1006"], # new 5 (4-е поколение)
            ("q1006",frozenset({"w", "s", "e", "n"})) : ["left", "q106"], # new 5 (4-е поколение)
            ("q106",frozenset({"s", "w", "e", "n"})) : ["down", "q16"],
            ("q16",frozenset({"e", "w", "s", "n"})) : ["right", "q16"],
            ("q16",frozenset({"w", "s"})) : ["down", "q16"],
            ("q16",frozenset({"n", "s"})) : ["up", "q106"],
            ("q106",frozenset({"n", "s", "w"})) : ["left", "q106"],
            ("q106",frozenset({"e", "s", "w"})) : ["down", "q16"],
            ("q16",frozenset({"w", "n", "e"})) : ["left", "q106"], # new 5 (3-е поколение)
            ("q16",frozenset({"w", "s", "e"})) : ["right", "q20"],
            ("q20",frozenset({"w", "s", "e"})) : ["right", "q20"],
            ("q20",frozenset({"w", "s", "e", "n"})) : ["right", "q20"],
            ("q20",frozenset({"w", "s", "n"})) : ["down", "q16"],
            ("q20",frozenset({"w", "s"})) : ["down", "q20"],
            ("q20",frozenset({"w", "e"})) : ["left", "q106"],
        }
        
        self.sixth_bypasser_program = {
            ("q10",frozenset({"s", "w", "e"})) : ["right", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
            ("q10",frozenset({"s", "w", "e", "n"})) : ["up", "q10"],
        }

        self.end_program = {
            ("q20",frozenset({"s", "w", "e"})) : ["right", "q14"],
            ("q200",frozenset({"s", "w", "e"})) : ["right", "q14"],
            ("q200",frozenset({"s", "w", "e", "n"})) : ["right", "q14"],
            ("q18",frozenset({"s", "w", "e"})) : ["right", "q14"],
            ("q19",frozenset({"s", "w", "e", "n"})) : ["right", "q14"],
            ("q19",frozenset({"s", "w", "e"})) : ["right", "q14"],
            ("q15",frozenset({"s", "w", "e"})) : ["right", "q14"],
            ("q18",frozenset({"s", "w", "e", "n"})) : ["right", "q14"],
            ("q17",frozenset({"s", "w", "e", "n"})) : ["right", "q14"],
            ("q17",frozenset({"s", "w", "e"})) : ["right", "q14"],
            ("q20",frozenset({"s", "w", "e", "n"})) : ["right", "q14"],
            ("q15",frozenset({"s", "w", "e", "n"})) : ["right", "q14"],
            ("q13",frozenset({"s", "e"})) : ["right", "q14"],
            ("q13",frozenset({"s", "e", "w"})) : ["right", "q14"],
            ("q13",frozenset({"s", "e", "w", "n"})) : ["right", "q14"],
            ("q14",frozenset({"s", "e"})) : ["right", "q14"],
            ("q14",frozenset({"s", "n"})) : ["up", "q14"],
            ("q14",frozenset({"s", "e", "w"})) : ["right", "q14"],
            ("q14",frozenset({"s", "e", "w", "n"})) : ["right", "q14"],
            ("q10",frozenset({"s", "e", "w", "n"})) : ["right", "q14"],
            ("q14",frozenset({"s", "w", "n"})) : ["up", "q14"]
        }