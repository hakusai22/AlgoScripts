# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:54

if __name__ == '__main__':

    teams = ['Barcelona', 'Bayern Munich', 'Chelsea', 'dasda']
    leagues = ['La Liga', 'Bundesliga', 'Premiere League', 'dasda']
    countries = ['Spain', 'Germany', 'UK', 'dasda']
    for team, league, country in zip(teams, leagues, countries):
        print(f'{team} plays in {league}. Country: {country}')
