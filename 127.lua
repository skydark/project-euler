function gcd(a, b)
    if b == 0 then
        return a
    else
        return gcd(b, a % b)
    end
end

function main(M)
    -- int rad[M];
    local rad = {}
    rad[1] = 1
    for p = 2, M-1 do
        rad[p] = 0
    end
    for p = 2, M-1 do
        if rad[p] == 0 then
            local isqrtp = math.floor(math.sqrt(p))
            local last_q = isqrtp + 1
            for q = 2, isqrtp do
                if p % q == 0 then
                    local pp = p
                    while pp % q == 0 do
                        pp = math.floor(pp / q)
                    end
                    local qq = q * rad[pp]
                    pp = p
                    while pp < M do
                        rad[pp] = qq
                        pp = pp * q
                    end
                    last_q = q
                    break
                end
            end
            if last_q > isqrtp then
                local pp = p
                while pp < M do
                    rad[pp] = p
                    pp = pp * p
                end
            end
        end
    end

    local s = 0
    for c = 3, M-1 do
        local cc = math.floor((c-1)/rad[c])
        if rad[c-1] <= cc then
            s = s + c
        end
        if cc >= 6 and not (c % 2 == 0 and cc < 15) and not (c % 3 == 0 and cc < 10) then
            for a = 2, math.floor(c / 2) - 1 do
                b = c - a
                if rad[a] <= cc and rad[b] <= cc and rad[a] <= math.floor(cc/rad[b]) and gcd(a, b) == 1 then
                    s = s + c
                end
            end
        end
    end
    return s
end

print(main(120000))

