import random

class CombatSystem:
    def test(self):
        print("Test CombatSystem")
    def __init__(self):
        self.battle_history = []

    def roll_to_hit(self, defender_armor, attacker=None):
        roll = random.randint(0, 20)
        threshold = 5 + defender_armor

        morale_modifier = 0
        if attacker and attacker.get('is_human'):
            morale = attacker.get('morale', 20)
            if morale <= 35:
                if morale <= 20:
                    morale_modifier -= 3
                if morale > 20:
                    morale_modifier += 2
            roll += morale_modifier

        if roll == 20:
            return True, roll, True, threshold, morale_modifier
        if roll < threshold:
            return False, roll, False, threshold, morale_modifier
        return True, roll, False, threshold, morale_modifier

    def calculate_damage(self, attacker_strength, weapon_bonus=0, morale=20):
        rng = random.randint(0, 10)
        morale_bonus = 2 if morale > 20 else 0
        morale_penalty = 0
        if morale <= 25:
            morale_penalty = 0.5

        damage = attacker_strength + weapon_bonus + morale_bonus + rng
        if morale <= 25:
            damage = int(damage * morale_penalty)

        return damage, rng, morale_bonus

    def apply_morale_hit_penalty(self, humans, target, loss_self, loss_others):
        for h in humans:
            if h['name'] == target['name']:
                h['morale'] = max(0, h['morale'] - loss_self)
            elif abs(h['position'] - target['position']) == 1:
                h['morale'] = max(0, h['morale'] - loss_others)

    def apply_morale_death_penalty(self, humans, dead_human):
        for h in humans:
            if h['name'] != dead_human['name'] and abs(h['position'] - dead_human['position']) == 1:
                h['morale'] = max(0, h['morale'] - 5)

    def melee_combat(self, attacker, defender, humans):
        hit, roll, critical, threshold, morale_mod = self.roll_to_hit(defender.get('armor', 0), attacker)

        if not hit:
            print(f"\n❌ {attacker['name']} rolled {roll} and missed {defender['name']} ({threshold})")
            return None

        damage, rng, morale_bonus = self.calculate_damage(
            attacker['strength'],
            attacker.get('weapon_bonus', 0),
            attacker.get('morale', 20)
        )

        armor_before = defender.get('armor', 0)
        if armor_before > 0 and not critical:
            if damage <= armor_before:
                defender['armor'] -= damage
                damage_to_health = 0
            else:
                damage_to_health = damage - armor_before
                defender['armor'] = 0
                defender['health'] -= damage_to_health
        else:
            damage_to_health = damage
            defender['health'] -= damage_to_health

        if defender.get('is_human') and damage_to_health > 0:
            self.apply_morale_hit_penalty(humans, defender, 2, 1)

        if attacker.get('is_human') and damage_to_health > 0:
            attacker['morale'] = attacker.get('morale', 20) + 3

        result = {
            'attacker': attacker['name'],
            'attacker_hp': attacker['health'],
            'attacker_pos': attacker['position'],
            'defender': defender['name'],
            'defender_pos': defender['position'],
            'weapon_bonus': attacker.get('weapon_bonus', 0),
            'random_factor': rng,
            'damage_dealt': damage,
            'damage_to_armor': min(damage, armor_before) if not critical else 0,
            'damage_to_health': damage_to_health,
            'defender_armor_after': defender.get('armor', 0),
            'defender_hp_after': defender['health'],
            'defender_dead': defender['health'] <= 0,
            'hit_roll': roll,
            'critical_hit': critical,
            'hit_threshold': threshold,
            'hit_result': "Hit landed" if damage_to_health > 0 or (armor_before > 0 and damage_to_health == 0) else "Miss",
            'attacker_morale': attacker['morale'] if 'morale' in attacker else None,
            'morale_mod_hitroll': attacker.get('morale_mod_hitroll', 0) if 'morale' in attacker else 0,
            'morale_bonus_damage': attacker.get('morale_bonus_damage', 0) if 'morale' in attacker else 0,
            'morale_penalty_damage': attacker.get('morale_penalty_damage', 0) if 'morale' in attacker else 0,
            'attacker_morale': attacker.get('morale', 20)
        }

        self.battle_history.append(result)
        return result

def print_turn(res):
    if res is None:
        return

    crit_text = " (CRITICAL HIT!)" if res['critical_hit'] else ""
    morale = res.get('attacker_morale', 20)
    morale_info = f" (Morale: {morale})"

    morale_note = ""
    if morale > 20:
        morale_note = " Buffs:"
        if res['morale_mod_hitroll'] > 0:
            morale_note += f" +{res['morale_mod_hitroll']} to Hit"
        if res['morale_bonus_damage'] > 0:
            morale_note += f" +{res['morale_bonus_damage']} Dmg"
    elif morale < 20:
        morale_note = " Debuffs:"
        if res['morale_mod_hitroll'] < 0:
            morale_note += f" {res['morale_mod_hitroll']} to Hit"
        if res['morale_penalty_damage'] < 0:
            morale_note += f" {res['morale_penalty_damage']} Dmg"

    print(f"\n- Attacker: {res['attacker']} (Weapon bonus: {res['weapon_bonus']}, RNG: {res['random_factor']})")
    print(f"- Hit Roll: {res['hit_roll']}{crit_text} -> {res['hit_result']} (Needs ≥ {res['hit_threshold']} to hit)")
    if res['attacker_morale'] is not None:
        print(f"- Morale: {res['attacker_morale']}", end='')
        if res['attacker_morale'] > 20:
            print(f" Buffs: +{res['morale_mod_hitroll']} to hit, +{res['morale_bonus_damage']} damage")
        elif res['attacker_morale'] <= 20:
            print(f" Penalties:", end='')
            if res['morale_mod_hitroll'] < 0:
                print(f" {res['morale_mod_hitroll']} to hit", end='')
            if res['morale_penalty_damage'] > 0:
                print(f", -{res['morale_penalty_damage']} damage", end='')
            print()

    print(f"- Total Damage dealt: {res['damage_dealt']} (Armor absorbed: {res['damage_to_armor']}, Health taken: {res['damage_to_health']})")
    print(f"- Defender Armor after: {res['defender_armor_after']} | HP after: {res['defender_hp_after']}")
    if res['defender_dead']:
        print(f" {res['defender']} has been defeated.")




def group_battle():
    print("\n=== Group Battle with Morale, Buffs, Armor, Infection, Hit Rolls ===")

    while True:
        try:
            num_humans = int(input("Enter number of humans (1-20): "))
            num_zombies = int(input("Enter number of zombies (1-20): "))
            if 1 <= num_humans <= 20 and 1 <= num_zombies <= 20:
                break
            else:
                print("Please enter numbers between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    cs = CombatSystem()

    humans = []
    for i in range(num_humans):
        humans.append({
            'name': f'Human{i}',
            'strength': random.randint(5, 7),
            'weapon_bonus': random.choice([0, 1, 2, 3]),
            'health': 30,
            'armor': random.randint(5, 10),
            'position': random.choice([1, 2, 3]),
            'infected': False,
            'morale': 20,
            'is_human': True
        })

    zombies = []
    for i in range(num_zombies):
        zombies.append({
            'name': f'Zombie{i}',
            'strength': random.randint(4, 6),
            'weapon_bonus': 0,
            'health': 25,
            'armor': random.randint(3, 8),
            'position': random.choice([-3, -2, -1]),
            'is_human': False
        })

    turn = 0
    round_num = 1

    while humans and zombies:
        print(f"\n--- Round {round_num} ---")
        round_num += 1

        if turn == 0:
            attacker = random.choice(zombies)
            defender = random.choice(humans)
        else:
            attacker = random.choice(humans)
            defender = random.choice(zombies)

        if attacker.get('morale', 20) <= 0:
            print(f" {attacker['name']} runs away due to broken morale!")
            if attacker['is_human']:
                humans.remove(attacker)
            turn = 1 - turn
            continue

        distance = abs(attacker['position'] - defender['position'])
        if distance > 1:
            if attacker['position'] < defender['position']:
                attacker['position'] += 1
            else:
                attacker['position'] -= 1
            print(f"{attacker['name']} moves closer to {defender['name']} (pos {attacker['position']})")
        else:
            res = cs.melee_combat(attacker, defender, humans)
            print_turn(res)

            if res and res['defender_dead']:
                if defender['is_human']:
                    cs.apply_morale_death_penalty(humans, defender)
                    humans.remove(defender)
                else:
                    zombies.remove(defender)

            if attacker['is_human'] and attacker['morale'] <= 0:
                print(f" {attacker['name']} panicked and ran away!")
                humans.remove(attacker)

            if not attacker['is_human'] and res and res['damage_to_health'] > 0:
                if random.randint(1, 9) == 9 and not defender['infected']:
                    defender['infected'] = True
                    print(f" {defender['name']} has been infected!")

        turn = 1 - turn

    print("\n Battle Ended")
    if humans:
        print(" Humans win!")
    else:
        print("☠ Zombies win!")

    if humans:
        print("\nSurviving Humans:")
        for h in humans:
            status = "Infected" if h['infected'] else "Healthy"
            print(f"- {h['name']} (HP: {h['health']}, Armor: {h['armor']}, Morale: {h['morale']}, Pos: {h['position']}) - {status}")
    else:
        print("\nNo humans survived.")

    if zombies:
        print("\nSurviving Zombies:")
        for z in zombies:
            print(f"- {z['name']} (HP: {z['health']}, Armor: {z['armor']}, Pos: {z['position']})")
    else:
        print("\nNo zombies survived.")

if __name__ == "__main__":
    group_battle()
