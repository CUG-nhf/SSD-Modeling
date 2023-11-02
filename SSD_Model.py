import numpy as np
from Math import Possion


class ssdModel:
	def __init__(self, BER, cnt, pe) -> None:
		
		self.block_error_rate = BER
		self.plane_error_rate = []
		self.die_error_rate = []
		self.chip_error_rate = []
		self.channel_error_rate = []
		self.ssd_error_rate = []
		
		if len(cnt) < 5:
			print("count error")
			return
		self.nblock = cnt[0]
		self.nplane = cnt[1]
		self.ndie = cnt[2]
		self.nchip = cnt[3]
		self.nchannel = cnt[4]

		if len(pe) != len(BER):
			print('length error')
			return
		self.PE = pe
	
	def getBlockErrorRate(self):
		return self.block_error_rate
	
	def getPlaneErrorRate(self):
		if self.plane_error_rate == []:
			Lambda = np.array(self.getBlockErrorRate()) * self.nblock / np.array(self.PE)
			self.plane_error_rate = [1 - Possion(Lambda[i], 0, self.PE[i]) for i in range(len(self.PE))]

		return self.plane_error_rate
	
	def getDieErrorRate(self):
		if self.die_error_rate == []:
			Lambda = np.array(self.getPlaneErrorRate()) * self.nplane / np.array(self.PE)
			self.die_error_rate = [1 - Possion(Lambda[i], 0, self.PE[i]) for i in range(len(self.PE))]

		return self.die_error_rate
	
	def getChipErrorRate(self):
		if self.chip_error_rate == []:
			Lambda = np.array(self.getDieErrorRate()) * self.ndie / np.array(self.PE)
			self.chip_error_rate = [1 - Possion(Lambda[i], 0, self.PE[i]) for i in range(len(self.PE))]

		return self.chip_error_rate

	def getChannelErrorRate(self):
		if self.channel_error_rate == []:
			Lambda = np.array(self.getChipErrorRate()) * self.nchip / np.array(self.PE)
			self.channel_error_rate = [1 - Possion(Lambda[i], 0, self.PE[i]) for i in range(len(self.PE))]

		return self.channel_error_rate

	def get_SSD_error_rate(self):
		if self.ssd_error_rate == []:
			Lambda = np.array(self.getChannelErrorRate()) * self.nchannel / np.array(self.PE)
			self.ssd_error_rate = [1 - Possion(Lambda[i], 0, self.PE[i]) for i in range(len(self.PE))]
		
		return self.ssd_error_rate
		
		

