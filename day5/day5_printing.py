
def get_middle(pages):
    middle_index = len(pages) // 2
    return pages[middle_index]


def sort_pages(pages, print_orders):
    for order in print_orders:
        first, second = order.split('|')
        try:
            if pages.index(first) > pages.index(second):
                index_first = pages.index(first)
                index_second = pages.index(second)
                pages[index_first], pages[index_second] = pages[index_second], pages[index_first]
                pages = sort_pages(pages, print_orders)
        except ValueError:
            continue
    return pages


def count_middles(print_orders):
    count = 0
    for pages in print_orders:
        middle = get_middle(pages)
        count += int(middle)
    return count


if __name__ == "__main__":
    count = 0
    ok_pages = []
    with open(r"day5\input") as f:
        data = f.read()
    print_order, page_book = data.split('\n\n')
    print_orders = print_order.split('\n')

    lines = page_book.split('\n')
    for line in lines:
        pages = line.split(',')
        for order in print_orders:
            ok = True
            first, second = order.split('|')
            try:
                if pages.index(first) > pages.index(second):
                    ok = False
                    break
            except ValueError:
                continue
        if ok:
            ok_pages.append(pages)

    print(f"First part: {count_middles(ok_pages)}")

    # Part 2:
    original_pages = []
    for line in lines:
        original_pages.append(line.split(','))

    wrong_list = [x for x in original_pages if x not in ok_pages]

    sorted_wrong_pages = []
    for lines in wrong_list:
        sorted_wrong_pages.append(sort_pages(lines, print_orders))

    print(f"Second part: {count_middles(sorted_wrong_pages)}")
