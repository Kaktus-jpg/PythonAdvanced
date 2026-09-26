import logging

root = logging.getLogger()
sub_1 = logging.getLogger("sub_1")
sub_1.setLevel(logging.INFO)
sub_2 = logging.getLogger("sub_2")
sub_sub_1 = logging.getLogger("sub_2.sub_sub_1")

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

for logger in (sub_1, sub_sub_1):
    logger.addHandler(handler)

formatter = logging.Formatter(
    fmt="%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s: %(lineno)d"
)
handler.setFormatter(formatter)


root_handler = logging.StreamHandler()
root_handler.setLevel(logging.DEBUG)
root_handler.setFormatter(formatter)
root.addHandler(handler)

sub_2.propagate = False
sub_1.propagate = True

all_loggers = (root, sub_1, sub_2, sub_sub_1)

for logger in all_loggers:
    logger.info(logger.name)
