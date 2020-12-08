import bags


def test_parse():
    rules = bags.get_input('example_input.txt')
    bag_list = bags.parse_bags(rules)
    assert len(bag_list) == 9
    assert len(bag_list['muted yellow'].inner_bags) == 2
    assert len(bag_list['muted yellow'].outer_bags) == 2


def test_count_countains():
    rules = bags.get_input('example_input.txt')
    bag_list = bags.parse_bags(rules)
    shiny_gold = bag_list['shiny gold']
    contain_count = bags.count_contains(shiny_gold)
    assert contain_count == 4


def test_count_inside():
    rules = bags.get_input('example_input.txt')
    bag_list = bags.parse_bags(rules)
    shiny_gold = bag_list['shiny gold']
    contain_count = bags.count_inside(shiny_gold)
    assert contain_count == 32
