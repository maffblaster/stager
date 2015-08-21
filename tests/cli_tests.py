# For testing, of course!
import unittest

CliTestCase(unittest.TestCase):
  def setUp():
      print("Prepare environment for every test in this class.")

  def tearDown():
      print("Clean up test environment.")

  def test_Version():
      print("Test ran!")
      
  def test_Verbose():
      print("Verbose...")
      
  def test_Quiet():
      print("Quiet")