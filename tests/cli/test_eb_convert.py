import argparse
from eb_model.cli.eb_convert import create_argument_parser, parse_arguments


def test_create_argument_parser():
    """Test that argument parser can be created."""
    parser = create_argument_parser()
    assert parser is not None
    assert parser.prog == "eb-convert"


def test_parse_arguments_basic():
    """Test parsing basic arguments."""
    args = parse_arguments(["input.xdm", "output_dir/"])
    assert args.inputs == ["input.xdm"]
    assert args.output_dir == "output_dir/"
    assert args.verbose is False
    assert args.log is None


def test_parse_arguments_with_options():
    """Test parsing arguments with options."""
    args = parse_arguments(["--verbose", "--log", "test.log", "input.xdm", "output_dir/"])
    assert args.inputs == ["input.xdm"]
    assert args.output_dir == "output_dir/"
    assert args.verbose is True
    assert args.log == "test.log"


def test_parse_arguments_multiple_inputs():
    """Test parsing multiple input files."""
    args = parse_arguments(["input1.xdm", "input2.xdm", "input3.xdm", "output_dir/"])
    assert args.inputs == ["input1.xdm", "input2.xdm", "input3.xdm"]


def test_parse_arguments_with_skip_os_task():
    """Test parsing with skip-os-task option."""
    args = parse_arguments(["--skip-os-task", "Os.xdm", "output_dir/"])
    assert args.skip_os_task is True


def test_parse_arguments_default_skip_os_task():
    """Test that skip-os-task defaults to False."""
    args = parse_arguments(["Os.xdm", "output_dir/"])
    assert args.skip_os_task is False