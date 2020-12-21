x = rand(1,3) * 10;
y = rand(1,3) * 10;

curr_point = rand(1,2) * 10;


plot(x, y, 'o');


for i = 1:10000
    
    j = 1 + floor((rand(1) * 3));
    
    plot(curr_point(1), curr_point(2), 'o');
    
    curr_point(1) = (curr_point(1) + x(j))/2;
    curr_point(2) = (curr_point(2) + y(j))/2;
    
    
end


