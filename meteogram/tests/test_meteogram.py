"""Test use of the meteogram module."""

import datetime
import numpy as np
from meteogram import meteogram
from numpy.testing import assert_almost_equal, assert_array_almost_equal


#
# Example starter test
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary


# Instructor led introductory examples
def test_title_case():
    # Setup
    input = 'this is a test string'
    desired = 'This Is A Test String'

    # Exercise
    actual = input.title()

    # Verify
    assert actual == desired

    # Cleanup - none necessary


def test_floating_subtraction():
    # Setup
    desired = 0.293

    # Exercise
    actual = 1 - 0.707

    # Verify
    assert_almost_equal(actual, desired)

    # Cleanup


# Exercise 1
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    # Setup
    start = datetime.datetime(2018, 1, 5, 1)
    end = datetime.datetime(2018, 1, 9, 1)
    station = 'FSD'
    # tip: first try the test with an empty truth_url,
    #      then run and see the result_url pytest returns (calculated one)
    #      test truth_url in the browser and verify it is correct
    #      update the truth_url with the correct value
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01'
                 '&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&'
                 'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
                 'sample=1min&what=view&delim=comma&gis=yes')

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    assert result_url == truth_url

    # Cleanup - none necessary


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # Setup
    start = datetime.datetime(2018, 11, 21, 1)
    end = datetime.datetime(2018, 12, 13, 1)
    station = 'FSD'
    # tip: first try the test with an empty truth_url,
    #      then run and see the result_url pytest returns (calculated one)
    #      test truth_url in the browser and verify it is correct
    #      update the truth_url with the correct value
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=11&day1=21&hour1=01'
                 '&minute1=00&year2=2018&month2=12&day2=13&hour2=01&minute2=00'
                 '&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
                 '&sample=1min&what=view&delim=comma&gis=yes')

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    assert result_url == truth_url


class TestWindComponents():
    def test_wind_components_north(self):
        # Setup
        speed = 10
        direction = 0

        # Exercise
        u, v = meteogram.wind_components(windspeed=speed, wind_direction=direction)

        # Verify
        true_u = 0
        true_v = - 10

        assert_almost_equal(u, true_u)
        assert_almost_equal(v, true_v)

    def test_wind_components_northeast(self):
        # Setup
        speed = 10
        direction = 45

        # Exercise
        u, v = meteogram.wind_components(speed, direction)

        # Verify
        true_u = -7.0710
        true_v = -7.0710
        assert_almost_equal(u, true_u, 3)
        assert_almost_equal(v, true_v, 3)

    def test_wind_components_threesixty(self):
        # Setup
        speed = 10
        direction = 360

        # Exercise
        u, v = meteogram.wind_components(speed, direction)

        # Verify
        true_u = 0
        true_v = -10
        assert_almost_equal(u, true_u)
        assert_almost_equal(v, true_v)

    def test_wind_components_zero_wind(self):
        # Setup
        speed = 0
        direction = 45

        # Exercise
        u, v = meteogram.wind_components(speed, direction)

        # Verify
        true_u = 0
        true_v = 0
        assert_almost_equal(u, true_u)
        assert_almost_equal(v, true_v)

        # Cleanup

    def test_wind_components_array(self):
        """Use array to have one test of wind components in one operations"""
        # Setup
        winds = np.array([10, 10, 10, 0])
        directions = np.array([0, 45, 360, 45])

        # Exercise
        u, v = meteogram.wind_components(winds, directions)

        # Verify
        true_u = np.array([0, -7.0710, 0, 0])
        true_v = np.array([-10, -7.0710, -10, 0])
        assert_array_almost_equal(u, true_u, 3)
        assert_array_almost_equal(v, true_v, 3)

#

#
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
