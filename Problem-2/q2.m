% Problem 2 : Error probability of random codes over a BSC channel

global plot_points;

% Given parameters.
n = 15;
k = 10;
p = 0.015;
N = 1000;

% Stores the probability of decoding error as E/N
avg_error  = [];

% Iterating tt times to find minimum average error, which will
% corrospond to the best possible code from these tt codes.
for tt = 1:5
    
    % Generating code C of cardinality 2^k
    C = CodeGenerator(2^k,n);
    % Counter to keep track of number of decoding errors
    E = 0;
    
    for nn = 1:N
        % Randomly selecting a codeword to transmit from C.
        c = C(randi(length(C)),:);
        
        % Simulating BSC with trasmitted codeword c and received codeword y
        % with bit-flip probability p.
        y = BSC(c,p);
        
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % If p > 0.5, a bit flip is more likely than no bit flip.
        % So, minimum Hamming distance decoding won't work in such cases.
        % So, we flip the bits of y and then employ the decoding.
        if p > 0.5
            for dd = 1:length(y)
                if y(dd) == '0'
                    y(dd) = '1';
                else
                    y(dd) = '0';
                end
            end
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        % Indicator variable : 1 if decoder makes error, 0 if no decoding error
        I = 0;
        
        % Simulating Minimum HammingDistanceDecoder with decoder input y
        % and the output estimate codeword 'estimate' in C.
        estimate = MinimumHammingDistanceDecoder(y,C);
        
        % Decoding error (decoder estimate not equal to transmitted codeword c)
        if strcmp(estimate,c)==0
            I = 1;
        end
        
        % Computing E = E + Indicator(estimate not equal to c);
        E = E + I;
    end
    
    % Computing average decoding error corrosponding to code C, bit-flip probablity p, n and k
    % from N iterations.
    avg_error = [avg_error E/N];
end

% Minimum average probablity of decoding error for the (n,k,p) tuple
% corrosponding to the best code C from tt iterations.
P_E = min(avg_error);

% Rate of Code = log2|C|/n
fprintf("\n Rate of Code = %g\n", log2(height(C))/n);
% BSC Channel capacity
fprintf("\n BSC Channel Capacity = 1 - H_2(%g) = %g\n",p, 1 + p*log2(p) + (1-p)*log2(1-p));
fprintf("\n Minimum average probability of error = %g\n", P_E);

plot_points = [plot_points P_E];
