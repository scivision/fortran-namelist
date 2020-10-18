program read_namelist
!! demo reading a namelist

integer :: u, Nx

real, allocatable :: x(:)
real :: y
character(200) :: p  !< arbitrary length, longer than needed
character(:), allocatable :: path

namelist /base/ x,y,p
namelist /sizes/ Nx

open(newunit=u, file="example.nml", action="read")

read(u, nml=sizes)

allocate(x(Nx))
read(u,nml=base)

close(u)

path = trim(p)

print *,x
print *, path

end program
