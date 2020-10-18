classdef TestUnit < matlab.unittest.TestCase

methods (Test)

function test_basic(tc)
file = "example.nml";
dat = read_namelist(file, "base");
tc.verifyEqual(dat.x, [1, 2, 3])

dat = read_namelist(file, "empty");
tc.verifyEmpty(fieldnames(dat))
end

function test_lint(tc)

info = checkcode("read_namelist.m");
tc.verifyEmpty(info)

end

end
end
