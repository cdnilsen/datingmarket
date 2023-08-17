import datetime

contractID = 1001
class endUser:
    def __init__(self, endUserID, userName, passwordHash, creditHash, inviterID, currentMatchmakerID, currentContractID):
        self.endUserID = endUserID
        self.userName = userName
        self.passwordHash = passwordHash
        self.creditHash = creditHash
        self.inviterID = inviterID
        self.currentMatchmakerID = currentMatchmakerID
        self.currentContractID = currentContractID

    def weighBid(offeringMatchmaker, monthlyBid, matchmakerCost, closingBid):
        bidAccepted = input("Accept a bid for $" + str(monthlyBid) + " monthly and a closing fee of $" + str(closingBid) + "? (y/n)")
        if bidAccepted == "y":
            newContract = Contract(contractID, datetime.now(), self.endUserID, offeringMatchmaker[matchmakerID], inviterID, monthlyBid, matchmakerCost, closingBid)
            self.currentContractID = newContract[contractID]
            self.currentMatchmakerID = offeringMatchmaker[matchmakerID]
            offeringMatchmaker.currentContracts.append(newContract)
            contractID += 1
            print("Bid accepted. New contract established.")
        elif bidAccepted != "n":
            print("Please enter 'y' or 'n'")
        else:
            print("No bid accepted")

    def chargeCard(amount):
        print("Charging $" + str(amount) + " to your card.")


class Contract:
    def __init__(self, contractID, dateEstablished, endUser, matchmakerID, inviterID, monthlyCost, matchmakerCost, closingCost):
        self.contractID = contractID
        self.dateEstablished = dateEstablished
        self.endUser = endUser
        self.subscriberID = subscriberID
        self.matchmakerID = matchmakerID
        self.inviterID = inviterID
        self.monthlyCost = monthlyCost
        self.matchmakerCost = matchmakerCost
        self.closingCost = closingCost

    def monthlyPayment():
        endUser.chargeCard(monthlyCost)
        matchmakerID.receivePayment(monthlyCost * 0.85)
        inviterID.receivePayment(monthlyCost * 0.05)

    def monthlyMatchmakerCharge():
        matchmakerID.chargeCard(matchmakerCost)

    def getHitched():
        endUser.chargeCard(closingCost)
        matchmakerID.receivePayment(closingCost * 0.85)
        inviterID.receivePayment(closingCost * 0.05)

class Matchmaker:
    def __init__(self, matchmakerID, matchmakerName, passwordHash, creditHash, currentContracts):
        self.matchmakerID = matchmakerID
        self.matchmakerName = matchmakerName
        self.passwordHash = passwordHash
        self.creditHash = creditHash
        self.inviterID = inviterID
        self.currentContractID = currentContracts
    
    def chargeCard():
        print("Charging $" + str(amount) + " to your card.")

    def offerBid(self, endUser, contractID, monthlyBid, matchmakerCost, closingBid):
        endUser.weighBid(self, monthlyBid, matchmakerCost, closingBid)

    def bidOnExistingContract(existingContract, newMatchmakerBid):
        if (newMatchmakerBid > existingContract[matchmakerCost]):
            existingContract[matchmakerCost] = newMatchmakerBid
            existingContract[matchmakerID] = self[matchmakerID]
            print("Bid accepted. New contract established.")
        else:
            print("Bid rejected.")

    def receivePayment(amount):
        print(str(matchmakerID) + "receives $" + str(amount))
